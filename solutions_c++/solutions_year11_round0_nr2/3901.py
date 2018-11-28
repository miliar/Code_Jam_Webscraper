#include<iostream>
#include<string>
#include<cstring>
#include<fstream>

using namespace std;

int main()
{


ifstream fi;
fi.open("B-small-attempt2.in");
ofstream fo;
fo.open("output.txt");
int caseNum = 1;

string str;
string cstr = "";
string dstr = "";
string nstr = "";
int t;
int c, d, n;

int j=0;
string costr[36] = {""};
string opstr[28] = {""};
string inpstr;
int cs = 0;
int os = 0;
string temp ="";
string temp1 ="";
char c1,c2;

string list = "";
int k = -1;

if(fi.good())
	{
	getline(fi,str);
	t = atoi(&str[0]);
	
	//cout<<"\nT="<<t<<endl;
	
	for(int i=0; i<t; i++)
		{cout<<"\n\ncase="<<caseNum;
		list = "";
		
		j = cs = os = 0;
		c = d = n = 0;
		inpstr ="";
		//cout<<"hi";
		cstr = dstr = nstr = "";

		for(int i0=0; i0<36; i0++) costr[i0] = "";
		for(int i0=0; i0<28; i0++) opstr[i0] = "";
			
		
		getline(fi,str);
		
		while(str[j]==' ') j++;
		
		while(str[j]!=' ')
			{cstr = cstr + str[j];
			j++;}
		c = atoi(&cstr[0]);
		
		//cout<<"  c="<<c;
		
		j++;
		
		for(int i1=0; i1<c; i1++)
			{
			costr[cs] = str[j];
			costr[cs] = costr[cs] + str[j+1];
			costr[cs] = costr[cs] + str[j+2];
			cs++;
			j = j+4;
			}
		
		
		while(str[j]==' ')j++;
		
		while(str[j]!=' ')
			{dstr = dstr + str[j];
			j++;}
		d = atoi(&dstr[0]);
		//cout<<"  d="<<d;
		
		j++;
		
		for(int i2=0; i2<d; i2++)
			{
			//cout<<"\nHERE\n";
			// temp = str[j+1];
			// opstr[i2] = str[j];cout<<"\nHERE\n";
			// temp1 = opstr[i2];
			// opstr[i2] = temp1 + temp ;cout<<"\nHERE\n";
			//os++;
			c1 = str[j];
			c2 = str[j+1];
			//cout<<"  c1="<<c1<<"  c2="<<c2;
			//cout<<"  opstri2 ="<<opstr[i2];
			opstr[i2].append(1,c1);
			//cout<<"  opstri2 ="<<opstr[i2];
			opstr[i2].append(1,c2);
			//cout<<"  opstri2 ="<<opstr[i2];
			j = j+3;
			temp ="";
			temp1 = "";
			}
			
			
		while(str[j]==' ') j++;
		
		while(str[j]!=' ')
			{
			nstr.append(1,str[j]);
			//nstr = nstr + str[j];
			j++;
			}
		n = atoi(&nstr[0]);
		cout<<"  n="<<n;
		
		while(str[j]==' ')j++;
		
		for(int i3=0; i3<n; i3++)
			{
			inpstr.append(1,str[j]);
			j++;
			}
		
		
		
		
		 //cout<<"\nc="<<c<<"  d="<<d<<"  n="<<n<<"  str="<<inpstr;
		// cout<<"   Combine Pairs : "<<costr[0];
		// cout<<"   Opp Pairs : "<<opstr[0];
		
		char x1,x2,x3;
		x1 = x2 = x3 = ' ';
		
		list = list + inpstr[0];
		k=0;
		
		for(int i4=1; i4<n; i4++)
			{
			k++;
			list[k] = inpstr[i4];
			//list = list + inpstr[i4];
			
			
			for(int i5=0; i5<c; i5++)
				{
				x1 = costr[i5][0];
				x2 = costr[i5][1];
				x3 = costr[i5][2];
				
				if((list[k]==x1 && list[k-1]==x2) || (list[k]==x2 && list[k-1]==x1))
					{
					list[k-1] = x3;
					list[k] = 'X';
					k--;
					}
				
				}
				
			for(int i5=0; i5<d; i5++)
				{
				x1 = opstr[i5][0];
				x2 = opstr[i5][1];
				
				if(list[k] == x1)
					{
					for(int i6=0; i6<k; i6++)
						{
						if(list[i6]==x2)
							{
							list = "";
							k=-1;
							break;
							}
						}
					}
				else
				if(list[k] == x2)
					{
					for(int i6=0; i6<k; i6++)
						{
						if(list[i6]==x1)
							{
							list = "";
							k=-1;
							break;
							}
						}
					}
				
				}
				
				
			
			}
		
		
		
		fo<<"Case #"<<caseNum<<": [";
		for(int i6=0; i6<k; i6++)fo<<list[i6]<<", ";
		if(k>=0)fo<<list[k]<<"]"<<endl;
		else fo<<"]"<<endl;
		caseNum++;
		
		// cout<<"\nLIST = ";
		// for(int i6=0; i6<=k; i6++)cout<<list[i6];
		// cout<<"  (k="<<k<<")"<<endl;
		
		}
		
	
	
	
	}

fi.close();
fo.close();

return 0;
}
