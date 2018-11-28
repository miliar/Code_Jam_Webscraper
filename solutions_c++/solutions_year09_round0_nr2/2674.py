#include <iostream>
#include <cstring>
using namespace std;

int H, W;
int cache[101 * 101];
int m[101 * 101];
char l[101 * 101];

int get(int x, int y) {
   return m[x * W + y];
}

int getPos(int x, int y) {
   return x * W + y;
}

int findsink(int x, int y) {
   if (!((x - 1 >= 0 && get(x, y) > get(x - 1, y))|| 
       (x + 1 < H && get(x, y) > get(x + 1, y)) || 
       (y - 1 >= 0 && get(x, y) > get(x, y - 1)) ||
       (y + 1 < W && get(x, y) > get(x, y + 1)))) {
      return getPos(x, y);
   }

   int minX = -1, minY = -1;
   int minVal = 10001;

   if (x + 1 < H && get(x + 1, y) <= minVal) {
      minX = x + 1;
      minY = y;
      minVal = get(x + 1, y);
   }
   if (y + 1 < W && get(x, y + 1) <= minVal) {
      minX = x;
      minY = y + 1;
      minVal = get(x, y + 1);
   }
   if (y - 1 >= 0 && get(x, y - 1) <= minVal) {
      minX = x;
      minY = y - 1;
      minVal = get(x, y - 1);
   }
   if (x - 1 >= 0 && get(x - 1, y) <= minVal) {
      minX = x - 1;
      minY = y;
      minVal = get(x - 1, y);
   }

   if (cache[getPos(minX, minY)] == -1)
      cache[getPos(minX, minY)] = findsink(minX, minY);

   return cache[getPos(minX, minY)];
}

void findsinkall() {
   for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
	 if (cache[getPos(i, j)] == -1) {
	    cache[getPos(i, j)] = findsink(i, j);
	 }
      }
   }
}

void label(int x, int y, int sink, char c) {
   if (x >= 0 && x < H && y >= 0 && y < W &&
       l[getPos(x, y)] == -1 && cache[getPos(x, y)] == sink) {
      l[getPos(x, y)] = c;

      label(x - 1, y, sink, c);
      label(x + 1, y, sink, c);
      label(x, y - 1, sink, c);
      label(x, y + 1, sink, c);
   }
}

void labelall() {
   char c = 'a';
   for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
	 if (l[getPos(i, j)] == -1) {
	    label(i, j, cache[getPos(i, j)], c);
	    ++c;
	 }
      }
   }
}

int main() {
   int n;

   cin >> n;

   for (int i = 0; i < n; ++i) {
      cin >> H >> W;

      for (int j = 0; j < H; ++j) {
	 for (int k = 0; k < W; ++k) {
	    cin >> m[j * W + k];
	 }
      }

      memset(cache, -1, H * W * sizeof(int));
      memset(l, -1, H * W * sizeof(char));

      findsinkall();
      labelall();

      cout << "Case #" << i + 1 << ":" << endl;
      for (int j = 0; j < H; ++j) {
	 for (int k = 0; k < W; ++k) {
	    if (k != 0)  cout << " ";
	    cout << l[getPos(j, k)] << " ";
	 }
	 cout << endl;
      }
   }

   return 0;
}
