#include <map>
#include <iostream>
#include <iomanip>

using namespace std;

float blob_left_end(int start, int end, int count, int d) {
  return (((float)start + (float)end) / 2) - (((float)((count - 1) * d)) / 2.0);
}

float blob_right_end(int start, int end, int count, int d) {
  return (((float)start + (float)end) / 2) + (((float)((count - 1) * d)) / 2.0);
}

float blob_time(int start, int end, int count, int d) {
  return (float)(((count - 1) * d) - (end - start)) / 2.0;
}

void doit () {
  int c, d;
  cin >> c >> d;
  float blobs[c][3]; // start, end, count
  for(int i = 0 ; i < c; ++i) {
    int p, v;
    cin >> p >> v;
    float half_width = (((float)(v-1)) / 2) * ((float)d);
    blobs[i][0] = p - half_width;
    blobs[i][1] = p + half_width;
    blobs[i][2] = half_width;
  }

  int i = 0;
  int num_blobs = c;
  while(i < (num_blobs-1)) {
    float overlap = (blobs[i][1] + d) - blobs[i+1][0];
    //    cout << i << ": " << overlap << endl;
    if(overlap > 0) {
      if(blobs[i+1][2] > blobs[i][2]) {
        float one_side_only = min(overlap, blobs[i+1][2] - blobs[i][2]);
        float split = overlap - one_side_only;
        blobs[i][0] -= ((split / 2) + one_side_only);
        blobs[i][1] = blobs[i+1][1] + (split / 2);
        blobs[i][2] = max(blobs[i][2], blobs[i+1][2]) + (split / 2);
      } else {
        float one_side_only = min(overlap, blobs[i][2] - blobs[i+1][2]);
        float split = overlap - one_side_only;
        blobs[i][0] -= (split / 2);
        blobs[i][1] = blobs[i+1][1] + (split / 2)  + one_side_only;
        blobs[i][2] = max(blobs[i][2], blobs[i+1][2]) + (split / 2);
      }
      //      cout << "merging " << i << endl;
      for(int j = i+1; j < (num_blobs-1); j++) {
        blobs[j][0] = blobs[j+1][0];
        blobs[j][1] = blobs[j+1][1];
        blobs[j][2] = blobs[j+1][2];
      }
      num_blobs--;
      if ( i > 0 ) { i--; }
    } else {
      i++;
    }
  }

  float time = 0;
  for(int i = 0; i < num_blobs; i++) {
    time = max(time, blobs[i][2]);
  }
  cout << time << endl;
}

int main () {
  int t;
  cin >> t;
  cout << setprecision(10);
  for(int i = 0; i < t; ++i) {
    cout << "Case #" << (i+1) << ": ";
    doit();
  }

  return 0;
}
