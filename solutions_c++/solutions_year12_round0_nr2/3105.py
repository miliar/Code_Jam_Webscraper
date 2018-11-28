#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <sstream>
#include <algorithm>
using namespace std;

int main()
{
ifstream fi("B-large.in");
ofstream fo("Blarge.out");
int t,i,n,s,p,j,temp,count,a,b,c;
vector<int> scores;
fi >> t;
for(i=0;i<t;++i)
{


count = 0;
fi >> n >> s >> p;

for(j=0;j<n;++j){fi >> temp; scores.push_back(temp);}
sort(scores.begin(),scores.end());
for(j=n-1;j>=0;--j)
{
// cout << scores[j] << " ";
// if(scores[j] / 3 >= p){count += 1;}
// else if(scores[j] % 3 == 1 || scores[j] % 3 == 2){if(scores[j] / 3 + 1 >= p){count += 1;}}
// else if(s > 0 && scores[j] % 3 == 2){if(scores[j]/3 + 2 >= p){count += 1; s-= 1;}}
a = scores[j]/3; b = a; c = a;
a += scores[j] % 3;
if(a-1 >= p){a--; b++;}
if(a>10){a-=1;b+=1;}if(b>10){b-=1;c+=1;}
if(a >= p){if(a-b == 2 || a-c == 2){--s;} if(s>=0){++count;} /*cout << a << " " << b << " " << c << endl;*/ continue;}
if(a-b == 0 && s > 0 && b > 0){++a; --b;}
// cout << a << " " << b << " " << c << endl;
// if(a-b >= 2 || a-c >= 2){if(s==0){--a;++b;}}

if(a >= p){count += 1; if(a-b == 2 || a-c == 2){--s;} }
}
fo << "Case #" << i+1 << ": " << count;
fo << endl;


scores.clear();
}
fi.close();
fo.close();
return 0;
}