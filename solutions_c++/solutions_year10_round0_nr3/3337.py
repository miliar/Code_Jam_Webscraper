#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0.out");
	
	int i;
	in >> i;
	for(int p = 1; p <= i; p++)
	{
            int r, k, n;
            in >> r >> k >> n;
            int people[n];
            for(int i = 0; i < n; i++)
            {           
                        int group;
                        in >> group;
                        people[i] = group;
            }
            
            int t = 0;
            int cost = 0;
            for(int i = 0; i < r; i++)
            {
                    int test = 0;
                    int total = 0;
                    int breakout = n;
                    while (test == 0)
                    {
                          if(total > k)
                          {
                                if(t == (0)) total = total - people[n-1];
                                else total = total - people[t-1];
                                cost = cost + total;
                                test = 1;
                          }
                          else if(breakout == 0)
                          {
                                cost = cost + total;
                                test = 1;
                          }
                          else
                          {
                                total = total + people[t];
                                if(t == (n-1)) t = 0;
                                else t++;
                          }
                          breakout--;
                    }
                    if(t == (0)) t = n-1;
                    else t--;
            }
            out << "Case #" << p << ": " << cost << "\n";
    }
	in.close();
	out.close();
	return 0;
}
