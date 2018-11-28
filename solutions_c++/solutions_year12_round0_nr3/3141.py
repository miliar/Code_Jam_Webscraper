#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <sstream>
using namespace std;

bool isRec(long n, long m)
{
int i,j;
int size = 0;
long thing = 1;
stringstream ncrap,mcrap;
string nstr,mstr,temp;
while(thing <= n){thing *= 10; size += 1;}
n = thing*n+n;
ncrap << n;
nstr = ncrap.str();
mcrap << m;
mstr = mcrap.str();
// cout << nstr << " " << mstr;
for(i=0;i<size;++i)
{
temp = "";
for(j=0;j<size;++j){temp += nstr[i+j];}

// cout << temp << " ";
if(temp == mstr){return true;}
}
return false;
}

int main()
{
long i,j,t,a,b,n,m,count=0;
ifstream fi("C-small.in");
ofstream fo("Csmall.out");
fi >> t;

// cout << isRec(13,31);

for(i=0;i<t;++i)
{
fi >> a >> b;
for(n=a;n<=b;++n)
{
for(m=n+1;m<=b;++m)
{
if(/*n != m && n < m &&*/isRec(n,m)){count += 1;}
}
}
fo << "Case #" << i+1 << ": " << count << endl;
count = 0;
}

return 0;
}