#include <iostream>
#include <fstream>
using namespace std;

char crules[1][3];
char orules[1][2];
int crule_num, orule_num;
bool check_crule(char one, char two, char &ret_val)
{
	for(int i=0;i<crule_num;i++)
		if((one==crules[i][0] && two==crules[i][1])||(one==crules[i][1] && two==crules[i][0]))
		{
			ret_val = crules[i][2];
			return true;
		}
	return false;
}
bool check_orule(char one, char *ret_val, int &ret_len)
{
	int count=0;
	for(int i=0;i<orule_num;i++)
	{
		if(one==orules[i][0])
			ret_val[count++]=orules[i][1];
		else if(one==orules[i][1])
			ret_val[count++]=orules[i][0];
	}
	ret_len = count;
	return count>0;
}
bool need_clear(char *rule, char *values, int rule_len, int val_len)
{
	for(int i=0;i<val_len;i++)
		for(int j=0;j<=rule_len;j++)
			if(values[i]==rule[j])
			{
				return true;
			}
	return false;
}
int main()
{
	ofstream myfile;
	myfile.open ("outputl");
	int cc=1, tc, in_len, out_len, len;
	char in_rule[10], out_rule[10], temp_o[10];
	char temp;
	for(cin>>tc;cc<=tc;cc++)
	{
		out_len=-1,len=0,in_len=0;
		int i=0,j=0;
		for(cin>>crule_num;i<crule_num;i++)
			cin>>crules[i];
		for(cin>>orule_num;j<orule_num;j++)
			cin>>orules[j];
		cin>>in_len;
		cin>>in_rule;
		for(int k=0;k<in_len;k++)
		{
			if(out_len==-1)
			{
				out_rule[++out_len]=in_rule[k];
				continue;
			}
			if(check_crule(in_rule[k],out_rule[out_len],temp))
			{
				out_rule[out_len]=temp;	
			}
			else if(check_orule(in_rule[k],temp_o, len))
			{
				if(need_clear(out_rule,temp_o, out_len, len))
				{
					out_len=-1;
				}
				else
					out_rule[++out_len]=in_rule[k];
			}
			else
				out_rule[++out_len]=in_rule[k];
		}
		myfile<<"Case #"<<cc<<": [";
		for(int f=0;f<=out_len;f++)
			if(f==0)
				myfile<<out_rule[f];
			else
				myfile<<", "<<out_rule[f];
		myfile<<"]\n";
	}
	return 0;
}

