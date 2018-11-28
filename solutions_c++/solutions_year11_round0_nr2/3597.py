#include<iostream>
#include<fstream>
#include<stdlib.h>
# define SIZE 110
using namespace std;

class stack
{
public:
char a[SIZE];
int tos; // Top of Stack

	stack();
	void push(char);
	char pop();
	int isempty();
	int isfull();
};
stack::stack()
{
tos=0; //Initialize Top of Stack
}

int stack::isempty()
{
return (tos==0?1:0);
}
int stack::isfull()
{
return (tos==SIZE?1:0);
}

void stack::push(char i)
{
if(!isfull())
{
a[tos]=i;
tos++;
}
else
{
 cout<<"Stack overflow error !Possible Data Loss !";
}
}
char stack::pop()
{
if(!isempty())
{
return(a[--tos]);
}
else
{
cout<<"Stack is empty! What to pop...!";
}
return 0;
}

int main()
{
	int t,iter=1,i,j;
	ifstream ifile ("smallB.txt");
	ofstream ofile ("output.txt");
	ifile>>t;
	int c,d,n;
	char replace[26][26];
	char input[110],ch,item;
	int oppose[26][26];
	
	while(t)
	{
		stack *s = new stack();		
		input[0] = '\0';		
		for(i=0;i<26;i++)
		{
			for(j=0;j<26;j++)
			{
				replace[i][j] = '$';
				oppose[i][j] = 0;
			}
		}
		ifile>>c;
		
		while(c)
		{
			ifile>>input;
			replace[input[0]-'A'][input[1]-'A'] = input[2];
			replace[input[1]-'A'][input[0]-'A'] = input[2];
			c--;
		}
		ifile>>d;
		
		while(d)
		{
			ifile>>input;
			oppose[input[0]-'A'][input[1]-'A'] = 1;
			oppose[input[1]-'A'][input[0]-'A'] = 1;
			d--;
		}
		ifile>>n;
		ifile>>input;
		/*
		for(i=0;i<26;i++)
			ofile<<(char)i+65<<"    ";
		ofile<<"\n";
		for(i=0;i<26;i++)
		{
			ofile<<(char)i+65<<" :";
			for(j=0;j<26;j++)
			{
				ofile<<replace[i][j]<<" "<< oppose[i][j]<<" "; 
			}
			ofile<<"\n";
		}
		*/
		for(i=0;input[i]!='\0';i++)
		{
			ch = input[i];
			s->push(ch);
			while(s->tos >= 2)
			{
				
				item = replace[s->a[s->tos-1]- 'A'][s->a[s->tos-2] - 'A'];
				//ofile<<item<<" ";
				if(item != '$')
				{
					s->pop();
					s->pop();
					s->push(item);
				}
				else
					break;
			}
			j=s->tos-2;
			//ofile<<s->tos<<" ";
			while(j >= 0)
			{
				if(oppose[s->a[s->tos-1]-'A'][s->a[j] - 'A'] == 1)
				{ 
					s->tos = 0;
					break;
				}
				j--;
			}
			//ofile<<s->tos<<"\n";
		}
		ofile<<"Case #"<<iter<<": [";
		for(i=0;i<(s->tos-1);i++)
		{
			ofile<<s->a[i]<<", ";
		}
		if(s->tos > 0)
		ofile<<s->a[s->tos-1];
		ofile<<"]\n";
		delete s;
		t--;
		iter++;
	}
	return 0;
}
		
