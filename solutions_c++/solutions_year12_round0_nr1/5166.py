#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<string>
#include<iostream>
#include<sstream>
#include<complex>

using namespace std;

const int inf = 2147483647;
const double eps = 1e-9;
const double pi = acos(-1.0);

const int maxn = 1000;
const int mod = 1000003;

int n, m,i ,j, k;
char s[111],s2[111];
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int ntest;
	cin>>ntest;
    getchar();	
	for(int test=1; test<=ntest; test++)
	{
		
        gets(s);
		n = strlen(s);
		for(i=0;i<n;i++)
		   s2[i] = ' ';
		for(i=0;i<n;i++)
		{
            if(s[i]=='a') s2[i] ='y';
            else if(s[i]=='b') s2[i] = 'h';
            else if(s[i]=='c') s2[i] = 'e';
            else if(s[i]=='d') s2[i] = 's';
            else if(s[i]=='e') s2[i] = 'o';
            else if(s[i]=='f') s2[i] = 'c';
            else if(s[i]=='g') s2[i] = 'v';
            else if(s[i]=='h') s2[i] = 'x';
            else if(s[i]=='i') s2[i] = 'd';
            else if(s[i]=='j') s2[i] = 'u';
            else if(s[i]=='k') s2[i] = 'i';
            else if(s[i]=='l') s2[i] = 'g';
            else if(s[i]=='m') s2[i] = 'l';
            else if(s[i]=='n') s2[i] = 'b';
            else if(s[i]=='o') s2[i] = 'k';
            else if(s[i]=='p') s2[i] = 'r';
            else if(s[i]=='q') s2[i] = 'z';
            else if(s[i]=='r') s2[i] = 't';
            else if(s[i]=='s') s2[i] = 'n';
            else if(s[i]=='t') s2[i] = 'w';
            else if(s[i]=='u') s2[i] = 'j';
            else if(s[i]=='v') s2[i] = 'p';
            else if(s[i]=='w') s2[i] = 'f';
            else if(s[i]=='x') s2[i] = 'm';
            else if(s[i]=='y') s2[i] = 'a';
            else if(s[i]=='z') s2[i] = 'q';
                        
        }

		cout<<"Case #"<<test<<": ";
		for(i=0;i<n;i++)
           cout<<s2[i];
        cout<<endl; 
	}
	return 0;
}
