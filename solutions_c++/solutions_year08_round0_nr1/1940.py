#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;
int indxx(char ** table, char *str);

void display(int n, int m)
{
	fstream f;
//	char *ch;
	f.open("answer.out",fstream::app|fstream::out);
	/*ch = strtok(str," ");
	while(ch)
	{
		f<<ch<<" ";
		ch = strtok(NULL," ");
	}*/
	f<<"Case #"<<m<<": ";
	f<<n<<"\n";
	f.close();
}

int main()
{
	fstream f;
	char str[102];
	char **table;
	int l,n,m,x,y,z,a,b,c;
	int *k;


	f.open("A-large.in",fstream::in);
	f.getline(str,102);
	sscanf(str,"%d",&a);
	l=1;
	while(l<=a)
	{
		//cout<<"case #"<<l<<":\n";
		f.getline(str,102);
		sscanf(str,"%d",&n);
		
		table = (char **)malloc(n * sizeof(char*));
		k = (int*) malloc(n*sizeof(int));
		for(c=0;c<n;c++)
			k[c] = 0;
		for(m=0;m<n;m++)
		{
			table[m] = (char*)malloc(100);
			f.getline(table[m],102);
		}

		f.getline(str,102);
		b=n;
		sscanf(str,"%d",&n);
		y=0;z=0;
		for(m=1;m<=n;m++)
		{
			f.getline(str,102);
			x = indxx(table, str);
			//cout<<"x="<<x<<endl;
			if(k[x] == 0)
			{
				k[x] =1; y++;
			}
			//cout<<y<<endl<<endl;
			if(y == b)
			{
				z++; y=1; 
				for(c=0;c<b;c++)
					k[c] = 0;
				k[x] =1;
			}
			
		}
		display(z,l);

		for(m=0;m<b;m++)
		{
			free(table[m]);
			table[m]=NULL;
		}free(table);
		table=NULL;
		free(k);
		k=NULL;

		l++;
	}

	f.close();
	return 0;
}

int indxx(char **table, char *str)
{
	int i;
	//cout<<str<<endl;
	for(i=0; ;i++)
	{
		/*cout<<i;
		cout<<str<<endl;
		cout<<table[i];*/
		if(!strcmp(table[i],str))
			return i;
	}
}
