#include <iostream>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;

struct Vine {
   Vine() {
      cin >> position;
      cin >> length;
      largestLengthReached = 0;
   }
   int position;
   int length;
   int largestLengthReached;

   bool Test();
};

typedef map<int, Vine*> Vineyard;

typedef set<Vine*> TestPool;

struct Test {
   Test() {
      reached = false;
      changed = false;
      int count;
      cin >> count;
      for (int i = 0; i < count; i++) {
         Vine* vine = new Vine();
         vineyard[vine->position] = vine;
      }
      cin >> distance;
   }

   ~Test() {
      for (Vineyard::iterator it = vineyard.begin(); it != vineyard.end(); it++) {
         delete it->second;
      }
   }
   Vineyard vineyard;
   TestPool testPool;
   bool reached;
   bool changed;
   int distance;

   void TestVine(Vine* vine);
   bool Run();
};

void
Test::TestVine(Vine* vine)
{
   testPool.erase(vine);
   int left = vine->position - vine->largestLengthReached;
   int right = vine->position + vine->largestLengthReached;
   if (right >= distance) {
      reached = true;
      return;
   }
   Vineyard::iterator it;
   for (it = vineyard.lower_bound(left); it != vineyard.end() && it->second->position <= right; it++) {
      Vine* other = it->second;
      int distance = abs(vine->position - other->position);
      int length = min(distance, other->length);
      if (length > other->largestLengthReached) {
         other->largestLengthReached = length;
         testPool.insert(other);
      }
   }
}

bool
Test::Run()
{
   Vine* first = vineyard.begin()->second;
   first->largestLengthReached = first->position;
   testPool.insert(first);

   while (!testPool.empty()) {
      TestVine(*testPool.begin());
      if (reached) {
         return true;
      }
   }
   return false;
}

int
main()
{
   int T;
   cin >> T;
   for (int i = 0; i < T; i++) {
      Test test;
      cout << "Case #" << i + 1 << ": " << (test.Run() ? "YES" : "NO") << endl; 
   }
   return 0;
}
