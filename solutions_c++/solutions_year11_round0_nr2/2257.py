#include <fstream>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
//#include<iostream>

int i,o,n,p1,p2,p3,a[100][100],b[100],pom,t,pr,p,ans[1000],m,kol[100];
string s,abc="QWERTYUIOPASDFGHJKLZXCVBNM";

int pos(char c)
{
    for (int i=0; i<abc.size(); i++)
	if (abc[i]==c) return i;
    return -1;
}

int main()
{
    cin >> t;
    while (o<t)
	{
	    o++;
	    for (int i=0; i<30; i++)
		for (int j=0; j<30; j++)
		    a[i][j]=-1;
	    for (int i=0; i<30; i++) {b[i]=0; kol[i]=0;}
	    cin >> n;
	    for (int i=0; i<n; i++)
		{
		    cin >> s;
		    p1=pos(s[0]);
		    p2=pos(s[1]);
		    p3=pos(s[2]);
		    a[p1][p2]=p3;
		    a[p2][p1]=p3;
		}
	    cin >> n;
	    for (int i=0; i<n; i++)
		{
		    cin >> s;
		    p1=pos(s[0]);
		    p2=pos(s[1]);
		    b[p1]=b[p1]|(1<<p2);
		    b[p2]=b[p2]|(1<<p1);
		}
	    cin >> n;
	    cin >> s;
	    pr=-1;
	    m=0;
	    pom=0;
	    for (int i=0; i<n; i++)
		{
		    p=pos(s[i]);
		    if (pr>-1 && a[pr][p]>=0) 
			{
			    kol[pr]--;
			    if (kol[pr]==0) pom=pom^(1<<pr); 
			    pom=pom|(1<<a[pr][p]); 
			    pr=a[pr][p]; 
			    kol[pr]++;
			    ans[m-1]=pr; 
			    continue;
			}
		    if ((pom&b[p])>0) 
			{
			    m=0; 
			    pom=0; 
			    for (int i=0; i<30; i++) kol[i]=0;
			    pr=-1;
			    continue;
			}
		    pom=pom|(1<<p); pr=p; 
		    ans[m]=p;
		    kol[p]++;
		    m++;
		}
	    cout << "Case #" << o << ": [" ;
	    if (m>0) cout << abc[ans[0]];
	    for (int i=1; i<m; i++)
		cout << ", " << abc[ans[i]];
	    cout << "] " << endl;
	}
}
