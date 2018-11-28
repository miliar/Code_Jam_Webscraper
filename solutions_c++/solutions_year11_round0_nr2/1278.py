#include <iostream>
#include <fstream>
using namespace std;

#define MAX_N 100
char com_a[MAX_N], com_b[MAX_N], com_res[MAX_N];
char op_a[MAX_N], op_b[MAX_N];
char str[MAX_N];
int size_com;
int size_op;

int combine(char a, char b)
{
	for (int i = 0 ; i < size_com; i ++)
	{
		if ((a == com_a[i] && b == com_b[i])
		|| (b == com_a[i] && a == com_b[i]))
		{
			return i;
		}
	}
	return -1;
}

int oppose(char a, char b)
{
	for (int i = 0 ; i < size_op; i ++)
	{
		if ((a == op_a[i] && b == op_b[i])
			|| (b == op_a[i] && a == op_b[i]))
		{
			return i;
		}
	}
	return -1;
}

int main()
{	
	int nCase;
	cin>>nCase;
	for (int Case = 1; Case <= nCase ; Case ++)
	{		
		cin>>size_com;
		for (int i = 0; i < size_com; i ++)
		{
			cin>>com_a[i]>>com_b[i]>>com_res[i];
		}		
		cin>>size_op;
		for (int i = 0; i < size_op; i ++)
		{
			cin>>op_a[i]>>op_b[i];
		}
		int size_str;
		cin>>size_str;
		int pos = -1;
		while(size_str--){
			cin>>str[++pos];
			int res = 0;
			while (res >=0){
				if (pos >= 1){
					res = combine(str[pos-1], str[pos]);
					if (res >=0)
					{
						-- pos;
						str[pos] = com_res[res];
					}
				}
				else
					res = -1;
			}
			for (int i = 0; i < pos; i ++){
				res = oppose(str[pos], str[i]);
				if (res >= 0)
					pos = -1;
			}
		}
		cout<<"Case #"<<Case<<": [";
		for (int i = 0; i <pos; i++){
			cout<<str[i]<<", ";
		}
		if (pos >= 0)
		cout<<str[pos];
		cout<<"]\n";
	}
	return 0;
}