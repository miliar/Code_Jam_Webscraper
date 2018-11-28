#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<stdio.h>
#define lint long long
#define MIN(x,y) x<y?x:y
#define MAX(x,y) x>y?x:y
#define LIMIT 100001

using namespace std;

lint t,n,m,l,h;
lint i,j,k;
double myprd,mylcm,mygcd,cost,lgcd,llcm,gllcm,lhcf,slcm;
lint xx,yy;

char ch;
lint arr[LIMIT],a[LIMIT],b[LIMIT],c[LIMIT],freq[LIMIT];
lint gcd(lint a, lint b)
{
        if(b == 0)
        {
                return a;
        }
        else
        {
                return gcd(b, a % b);
        }
}

lint fun()
{
	cost = 0;
	for(i = l; i <= h;i++)
	{
		cost = 0;
		for(j = 0;j < n;j++)
		{
			if(freq[j]%i == 0 || i%freq[j] == 0)
			{
				cost = i;
			}
			else
			{
				cost = 0;
				break;
			}
		}
		if(cost != 0)
			return i;
	}
	return 0;		
			/*
				xx = MAX(mygcd,i);
				yy = MIN(mygcd,i);
				lgcd = gcd(xx,yy);
				slcm = mygcd * i/lgcd;
				xx = MAX(mylcm,i);
				yy = MIN(mylcm,i);
				lhcf = gcd(xx,yy);
				llcm = mylcm * i/lhcf;
				
				if(i == 10)
				{										
				}
				
				cout << "\nmygcd:"<<mygcd << " mylcm:"<<mylcm<<endl;
				cout << "\nslcm:"<<slcm << " lhcf:"<<lhcf<<endl;
				cout << "\nlgcd:"<<lgcd << " llcm:"<<llcm<<endl;
				if(lhcf == slcm && lgcd == mygcd && llcm == mylcm)
				{					
					return i;
				}
				*/
}

int main()
{
	//cout << "\nDone " << lmax << endl;
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;
	k = 0;
	while(k<t){
	//cost = 0;
	cin >> n >> l >> h;
	for(i = 0;i < n;i++)
	{
		cin >> freq[i];
	}
	//cout <<"\nInput :"<<input << " n:"<<n;
	k++;
	cost = fun();
	cout<<"\nCase #"<<k<<": ";
	if(cost == 0)
	{
		cout << "NO";
	}
	else
		cout << cost;
	cout << endl;
	}
}
