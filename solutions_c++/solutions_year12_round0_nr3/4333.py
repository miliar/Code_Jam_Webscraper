#include<iostream>
#include<fstream>
#include<vector>
#include <algorithm>
using namespace std;


typedef struct pair{
	unsigned long long int n;
	unsigned long long int m;
	pair(unsigned long long int a,unsigned long long int b)
	{
		n=a;
		m=b;
	}
}PAIR;

vector<PAIR> numbers;

bool MyDataSortPredicate(const PAIR& d1, const PAIR& d2)
{
  return d1.n < d2.n;
}

bool invector(const PAIR& p)
{
	for (unsigned long long int i=0; i<numbers.size(); i++)
		if (numbers[i].m==p.m && numbers[i].n==p.n) {return true;}

	return false;
}

int main()
{
	ifstream in;
	in.open("C-small-attempt0.in");
	ofstream out;
	out.open("output.txt");

	unsigned long long int cases = 0;
	in>>cases;

	for (unsigned long long int _case=0; _case<cases; _case++)
	{
		numbers.clear();

		unsigned long long int A,B,count=0;
		in>>A>>B;
		//cout<<A<<" "<<B<<endl;

		//if (_case==3)
		for (unsigned long long int n=A; n<=B; n++)
		{
			//cout<<i<<endl;
			char* str=new char[10000];
			itoa(n,str,10);

			// check if all are same
			char check = str[0];
			bool valid = false;
			for (unsigned long long int j=0; j<strlen(str); j++)
			{
				if (str[j]!=check) {valid = true;break;}
			}
			if (!valid) {continue;}

			for (unsigned long long int j=0; j<strlen(str); j++)
			{
				char *s = new char[10000];
				for (unsigned long long int k=0; k<strlen(str); k++)
				{
					//cout<<" "<<j<<" "<<k<<endl;
					unsigned long long int pos = (k+j)%strlen(str);
					s[k]=str[pos];
				}
				s[strlen(str)]='\0';
				unsigned long long int m = atoi(s);
				
				//if (n==1234) cout<<n<<","<<m<<endl;

				// A <= n < m <= B.
				if (A<m && m<=B && n<m)
				{
					if (!invector(PAIR(n,m)))
					{
					//out<<n<<","<<m<<endl;
						count++;
						
						//out<<p.n<<","<<p.m<<endl;
						numbers.push_back(PAIR(n,m));
						
					}
				}
			}

			delete str;
		}
			std::sort(numbers.begin(), numbers.end(), MyDataSortPredicate);
			
			for (unsigned long long int j=0; j<numbers.size(); j++)
			{
				//out<<numbers[j].m<<endl;
				//out<<numbers[j].n<<","<<numbers[j].m<<endl;
				//out<<numbers[j]<<","<<inverted[j]<<endl;
			}

		cout<<"Case #"<<_case+1<<": "<<count<<endl;
		out<<"Case #"<<_case+1<<": "<<count<<endl;
	}

	out.close();
	in.close();
}