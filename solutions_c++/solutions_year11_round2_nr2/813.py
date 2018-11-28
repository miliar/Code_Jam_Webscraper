#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
using namespace std;


const double eps=1e-7;
vector<double>a,b;
double d,t;
int n;
bool check(double m)
{
    int i;
    b[0]=a[0]-m;
    for(i=1;i<n;i++)
    {
        if(a[i]+m<b[i-1]+t) return false;
        b[i]=max(a[i]-m,b[i-1]+t);
    }
    return true;
}

int main()
{
    int cs,i,j;
    scanf("%d",&cs);
    for(int tt=1;tt<=cs;tt++){
	a.clear() ; b.clear();
    	cout << "Case #"<<tt <<": "; 
        scanf("%d%lf",&n,&t);
        for(i=0;i<n;i++){
		int xx,nn;
		cin >> xx >> nn;
		for(j=0;j<nn;j++)
			a.push_back(xx);
	}
	n=a.size();
	b = vector<double>(n);
        double l=0,h=n*(t+10.0),m;
        while(fabs(l-h)>eps)
        {
            m=(l+h)/2;
            if(check(m)) h=m;
            else l=m;
        }
        cout << m << "\n";
    }



    return 0;
}






