#include <iostream>

using namespace std;

int a[100];
int len;


void init()
{
	char s[100];
	cin.getline(s,100);
	len=0;
	for (int i=0;s[i];i++, len++)
		a[i] = s[i]-'0';
}
void print()
{
     for (int i=0;i<len;i++)
         cout<<a[i];
     cout<<endl;
}
void calc()
{

	for (int i=len-1;i>0;i--)
		if (a[i-1]<a[i])		
			for (int j=len-1;j>=i;j--)
				if (a[j]>a[i-1])
				{
					swap(a[j],a[i-1]);
					sort(a+i,a+len);
					print();
                    return;		
				}
	sort(a,a+len);
	for (int i=len;i>0;i--)
	    a[i] = a[i-1];
      a[0] = 0;
      len++;
      for (int i=0;i<len;i++)
          if (a[i]!=0) 
          {
                       swap(a[i],a[0]);
                       break;
          }
          
     print();
}
int main()
{
	int t;
	char s[10];
	cin>>t;
	cin.getline(s,10);
	for (int i=0;i<t;i++)
	{
		init();
		cout<<"Case #"<<i+1<<": ";
		calc();
	}
}
