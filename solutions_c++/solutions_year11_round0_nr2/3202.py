#include <iostream>
#include<cmath>
#include<set>
#include<vector>
#include<map>
#include<algorithm>
#include<string>

using namespace std;

vector<char> str1,str2,str3;
vector<char> cstr1,cstr2;
int cmb, cnl, len;
int i, k;
vector<char> str,res;
char checknonbase(char a, char b);
bool checkcancl(char a, int b);

int main()
{
	if(freopen("C:\\SANDBOX\\chocolates\\Debug\\input.txt", "r", stdin)&&freopen("C:\\SANDBOX\\chocolates\\Debug\\output.txt", "w", stdout))
	{
		//cout<<"Sucess!!";
	}
	else
	{
		cout<<"Fail!!";
		return 0;
	}

int num;
char a1,a2,a3,b1,b2,c1;
int sn;
sn = 1;

cin>>num;
while(num--)
{
	str1.clear();str2.clear();str3.clear();
	cin>>cmb;
	if(cmb)
	{
		for(i = 0; i < cmb; i++)
		{
			cin>>a1>>a2>>a3;
			str1.push_back(a1);str2.push_back(a2);str3.push_back(a3);
		}
	}
	cstr1.clear();cstr2.clear();
	cin>>cnl;
	if(cnl)
	{
		for(i = 0; i < cnl; i++)
		{
			cin>>b1>>b2;
			cstr1.push_back(b1);cstr2.push_back(b2);
		}
	}

	str.clear();
	cin>>len;
	for(i = 0; i < len; i++)
	{
		cin>>c1;
		str.push_back(c1);
	}

	res.clear();
	for(i = 1; i < len; i++)
	{
		if(c1 = checknonbase(str[i-1],str[i]))
		{
			str[i-1] = '0';
			str[i] = c1;
		}
		else if(checkcancl(str[i],i))
		{
			str[i] = '1';
		}
	}

	for(i = 0; i < len; i++)
	{
		if(str[i] == '0')
		{
			continue;
		}
		else if(str[i] == '1')
			res.clear();
		else
			res.push_back(str[i]);
	}


	cout<<"Case #"<<sn<<": [";
	if(res.size())
	{
		for(i = 0; i < res.size()-1; i++)
		{
			cout<< res[i]<<", ";
		}
		cout<<res[i];
	}
	cout<<"]"<<endl;
	sn++;
}
}

char checknonbase(char a, char b)
{
	for(k = 0;k < cmb; k++)
	{
		if((str1[k] == a && str2[k] == b)||(str1[k] == b && str2[k] == a))
			return str3[k];
	}
	return 0;
}

bool checkcancl(char a, int b)
{
	int j;
	for(j = b; j > 0; j--)
	{
		if(str[j] == '1')
			break;
	}

	for(; j < b; j++)
	for(k = 0;k < cnl; k++)
	{
		if((a == cstr1[k] && str[j] == cstr2[k]) || (a == cstr2[k] && str[j] == cstr1[k]))
			return true;
	}
	return false;
}