#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    freopen("ina","r",stdin);
    freopen("outa","w",stdout);
    int i,t,cas,n,k,j,m,l;
    string s[100];
	scanf("%d",&t);
	for (cas=1; cas<=t; cas++)
	{
	    scanf("%d%d",&n,&m);
        for (i=0; i<n; i++) cin>>s[i];
        char data[100][100]={0};
        for (i=n-1; i>=0; i--)
        {
            k=n-1;
            for (j=n-1; j>=0; j--)
            {
                if (s[i][j]!='.') data[k--][n-i-1]=s[i][j];
            }
            while (k>=0) data[k--][n-i-1]='.';
        }
        string b,r;
        for (i=0; i<m; i++) b+="B";
        for (i=0; i<m; i++) r+="R";
        bool foundb=0,foundr=0;
        for (i=0; i<n; i++)
        {
            string a(data[i]);
            if (a.find(b)!=-1) foundb=1;
            if (a.find(r)!=-1) foundr=1;
            a="";
            for (j=0; j<n; j++) a.push_back(data[j][i]);
            if (a.find(b)!=-1) foundb=1;
            if (a.find(r)!=-1) foundr=1;
        }
        for (l=0; l<n; l++)
        {
            string a;
            i=l;
            j=0;
            while (i>=0)
            {
                a.push_back(data[i][j]);
                i--;
                j++;
            }
            if (a.find(b)!=-1) foundb=1;
            if (a.find(r)!=-1) foundr=1;
        }
        for (l=0; l<n-1; l++)
        {
            string a;
            i=n-1;
            j=l+1;
            while (j<n) a.push_back(data[i--][j++]);
            if (a.find(b)!=-1) foundb=1;
            if (a.find(r)!=-1) foundr=1;
        }

        for (l=0; l<n; l++)
        {
            string a;
            i=l;
            j=n-1;
            while (i>=0) a.push_back(data[i--][j--]);
            if (a.find(b)!=-1) foundb=1;
            if (a.find(r)!=-1) foundr=1;
        }
        for (l=0; l<n-1; l++)
        {
            string a;
            i=n-1;
            j=n-l-1;
            while (j>=0) a.push_back(data[i--][j--]);
            if (a.find(b)!=-1) foundb=1;
            if (a.find(r)!=-1) foundr=1;
        }
        printf("Case #%d: ",cas);
        if (foundb && foundr) printf("Both\n");
        else if (foundb) printf("Blue\n");
        else if (foundr) printf("Red\n");
        else printf("Neither\n");
	}
	return 0;
}
