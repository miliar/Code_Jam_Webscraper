#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<stdlib.h>
#include<sstream>

using namespace std;

int main()
{
	int noc;
	cin >> noc;
	int cnt = 0;
	while(noc--)
	{
		cnt ++;
		int count = 0;
		char buf[33];
		int A,B,num,i,j;
		char a[10],b[10];
		cin >> a >> b;
		A=0;
		B=0;
		A = atoi(a);
		B = atoi(b);
//		cout << A << "   " << B << endl;
		char arr[10];
		for(i=A;i<=B;i++)
		{
//			i = 489;
			sprintf(a,"%d",i);
//			cout << a << endl;
			while(1)
			{
				int k = 1;
				arr[0] = a[strlen(a) -1];
				for(j=0;j<strlen(a)-1;j++)
				{
					arr[k] = a[j];
					k++;
				}
				arr[k] = '\0';
				strcpy(a,arr);
				num = 0;
				num = atoi(a);

				if(num == i)
					break;
				if(num <= B && num >= A && num >= i)
				{
					count ++;
//					cout << "this is a number " << num << endl;
				}

//				cout << num << endl;
			}
		

		}
		printf("Case #%d: ",cnt);
		cout <<  count << endl;
	}
}
