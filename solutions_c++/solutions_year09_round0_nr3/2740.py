#include <stdio.h>
#include <cstring>
#include <iostream>

#include <vector>
using namespace std;

void findpos(char case1[],vector<int> &a_pos,vector<int> &c_pos,vector<int>& d_pos,vector<int> &e_pos,vector<int> &j_pos,vector<int> &l_pos,vector<int> &m_pos,vector<int> &o_pos,vector<int> &t_pos,vector<int> &w_pos,vector<int>&space_pos);

long countNumber(char c,int pos,vector<int> &a_pos,vector<int> &c_pos,vector<int>& d_pos,vector<int> &e_pos,vector<int>&j_pos,vector<int>&l_pos,vector<int>&m_pos,vector<int> &o_pos,vector<int>&t_pos,vector<int>&w_pos,vector<int>&space_pos);

void strNumber(long result);

int main()
{
	
	vector<int> a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos;
//	char s[]="welcome to code jam";

	FILE *fp;
	fp=fopen("C-small-attempt1.in","r");
	
	char temp[101];
	int count=1;

	fgets(temp,100,fp);
	while(fgets(temp,100,fp)!=NULL)	
	{
		findpos(temp,a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);
		cout<<"Case #"<<count++<<": ";
		strNumber(countNumber('a',-1,a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos));
		cout<<"\n";
	
		a_pos.clear();
		c_pos.clear();
		d_pos.clear();
		e_pos.clear();
		j_pos.clear();
		l_pos.clear();
		m_pos.clear();
		o_pos.clear();
		t_pos.clear();
		w_pos.clear();
		space_pos.clear();

	}		
	return 0;
}

void findpos(char case1[],vector<int> &a_pos,vector<int> &c_pos,vector<int> &d_pos,vector<int> &e_pos,vector<int> &j_pos,vector<int> &l_pos,vector<int> &m_pos,vector<int> &o_pos,vector<int> &t_pos,vector<int> &w_pos,vector<int> &space_pos)

{
	int i=0;
	while(case1[i]!='\0')
	{
		switch(case1[i])
		{
			case 'a':
				a_pos.push_back(i);
				break;
			case 'c':
				c_pos.push_back(i);
				break;
			case 'd':
				d_pos.push_back(i);
				break;
			case 'e':
				e_pos.push_back(i);
				break;	
			case 'j':
				j_pos.push_back(i);
				break;
			case 'l':
				l_pos.push_back(i);
				break;
			case 'm':
				m_pos.push_back(i);
				break;
			case 'o':
				o_pos.push_back(i);
				break;
			case 't':
				t_pos.push_back(i);
				break;
			case 'w':
				w_pos.push_back(i);
				break;
			case ' ':	
				space_pos.push_back(i);
				break;
		}
		i++;
	}
}

long countNumber(char c,int pos,vector<int> &a_pos,vector<int> &c_pos,vector<int> &d_pos,vector<int> &e_pos,vector<int> &j_pos,vector<int> &l_pos,vector<int> &m_pos,vector<int> &o_pos,vector<int> &t_pos,vector<int> &w_pos,vector<int> &space_pos)

{
	//cout<<endl<<"now:"<<c<<endl;
	long num=0;
	switch(c)
	{
		case 'a':	
			for(int i=0;i<w_pos.size();i++)		
			{
				if(w_pos[i]>pos)	
				{
					for(int j=i;j<w_pos.size();j++)
						num+=countNumber('b',w_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
	
		case 'b':	
			for(int i=0;i<e_pos.size();i++)		
			{
				if(e_pos[i]>pos)	
				{
					for(int j=i;j<e_pos.size();j++)
						num+=countNumber('c',e_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'c':	
			for(int i=0;i<l_pos.size();i++)		
			{
				if(l_pos[i]>pos)	
				{
					for(int j=i;j<l_pos.size();j++)
						num+=countNumber('d',l_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'd':	
			for(int i=0;i<c_pos.size();i++)		
			{
				if(c_pos[i]>pos)	
				{
					for(int j=i;j<c_pos.size();j++)
						num+=countNumber('e',c_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'e':	
			for(int i=0;i<o_pos.size();i++)		
			{
				if(o_pos[i]>pos)	
				{
					for(int j=i;j<o_pos.size();j++)
						num+=countNumber('f',o_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'f':	
			for(int i=0;i<m_pos.size();i++)		
			{
				if(m_pos[i]>pos)	
				{
					for(int j=i;j<m_pos.size();j++)
						num+=countNumber('g',m_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'g':	
			for(int i=0;i<e_pos.size();i++)		
			{
				if(e_pos[i]>pos)	
				{
					for(int j=i;j<e_pos.size();j++)
						num+=countNumber('h',e_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'h':	
			for(int i=0;i<space_pos.size();i++)		
			{
				if(space_pos[i]>pos)	
				{
					for(int j=i;j<space_pos.size();j++)
						num+=countNumber('i',space_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'i':	
			for(int i=0;t_pos.size();i++)		
			{
				if(t_pos[i]>pos)	
				{
					for(int j=i;j<t_pos.size();j++)
						num+=countNumber('j',t_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'j':	
			for(int i=0;i<o_pos.size();i++)		
			{
				if(o_pos[i]>pos)	
				{
					for(int j=i;j<o_pos.size();j++)
						num+=countNumber('k',o_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'k':	
			for(int i=0;i<space_pos.size();i++)		
			{
				if(space_pos[i]>pos)	
				{
					for(int j=i;j<space_pos.size();j++)
						num+=countNumber('l',space_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'l':	
			for(int i=0;i<c_pos.size();i++)		
			{
				if(c_pos[i]>pos)	
				{
					for(int j=i;j<c_pos.size();j++)
						num+=countNumber('m',c_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'm':	
			for(int i=0;i<o_pos.size();i++)		
			{
				if(o_pos[i]>pos)	
				{
					for(int j=i;j<o_pos.size();j++)
						num+=countNumber('n',o_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'n':	
			for(int i=0;i<d_pos.size();i++)		
			{
				if(d_pos[i]>pos)	
				{
					for(int j=i;j<d_pos.size();j++)
						num+=countNumber('p',d_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'p':	
			for(int i=0;i<e_pos.size();i++)		
			{
				if(e_pos[i]>pos)	
				{
					for(int j=i;j<e_pos.size();j++)
						num+=countNumber('q',e_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'q':	
			for(int i=0;i<space_pos.size();i++)		
			{
				if(space_pos[i]>pos)	
				{
					for(int j=i;j<space_pos.size();j++)
						num+=countNumber('r',space_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 'r':	
			for(int i=0;i<j_pos.size();i++)		
			{
				if(j_pos[i]>pos)	
				{
					for(int j=i;j<j_pos.size();j++)
						num+=countNumber('s',j_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 's':	
			for(int i=0;i<a_pos.size();i++)		
			{
				if(a_pos[i]>pos)	
				{
					for(int j=i;j<a_pos.size();j++)
						num+=countNumber('t',a_pos[j],a_pos,c_pos,d_pos,e_pos,j_pos,l_pos,m_pos,o_pos,t_pos,w_pos,space_pos);			
					break;
				}		
			}
			break;
		case 't':	
			for(int i=0;i<m_pos.size();i++)		
			{
				if(m_pos[i]>pos)	
				{
					for(int j=i;j<m_pos.size();j++)
						num+=1;			
					break;
				}		
			}
			break;
	}
	return num;
}


void strNumber(long result)
{
	result%=10000;	
	char s[5];
	
	sprintf(s,"%ld",result);

	if(result/10==0)				
	{
		char tmp[]="000";
		cout<<strcat(tmp,s);	
	}

	else if(result/100==0)
	{
		char tmp[]="00";			
		cout<<strcat(tmp,s);
	}
	else if(result/1000==0)
	{
		char tmp[]="0";			
		cout<<strcat(tmp,s);
	}
	else
		cout<<s;	
}

