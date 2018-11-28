#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class node
{
 public:
 bool c[26];
 node* n[26];
 node(){ for(int i = 0; i < 26; i++) c[i] = false;
         for( int j = 0; j< 26; j++) n[j] = NULL; }     
 ~node()
	{ 
	 for(int i = 0; i < 26; i++)
	 {
		 if( n[i]!= NULL )
			 (*n[i]).~node();
	 }
	}
};

class pattern
{
public:
      int* k;
      char** c;
      int ll;
      pattern(int l){ll = l; k = new int[l]; c = new char*[l];}
      ~pattern(){ for( int i = 0; i < ll; i++) delete [] c[i];delete [] c; delete [] k;}
};

int check(pattern *p, node* root,int level,int maxLevel)
{
    node *r = root;
    int counter = 0;
    for( int i = 0; i< p->k[level];i++)
    {
     if( r->c[p->c[level][i] - 97] )
     {
         if( level < maxLevel)
             counter+=check(p,r->n[p->c[level][i]-97],level+1,maxLevel);
         else
             counter++;
     }         
    }   
    return counter;
}


int main(int argc, char *argv[])
{
    ifstream inputf(argv[1],ios::in);
	int L,D,N;
	inputf >> L;
	inputf>>D;
	inputf>>N;

	node root = node();
	for( int i = 0; i < D; i++)
	{
		node* r = &root;
		char s[L+1];
		inputf>>s;
		for( int j = 0; j < L; j++)
		{
			int tmp = s[j]-97;
			r->c[tmp] = true;
			if( r->n[tmp] == NULL && j!= L-1 )
				r->n[tmp] = new node();
			r = r->n[tmp];
		}
		r = &root; 
	}

    ofstream outputf("A-largeOut.out");

	for( int numN = 0; numN < N; numN++)
	{

		char t;
		pattern *p = new pattern(L);

		inputf.get(t);
		for( int kk=0; kk < L;kk++)
		{
			inputf.get(t);
			if( t==40)
			{
				inputf.get(t);
				int counter = 0;;
				bool cc[26];
				for(int i= 0; i < 26; i++) 
					cc[i] = false;
				while( t!= 41 )
				{
					if( cc[ t-97 ] == false )
					{
						cc[t-97] = true; counter++;
					}
					inputf.get(t);       
				} 
				p->k[kk] = counter;
				p->c[kk] = new char[counter];
				for( int i = 0,z = 0; i < 26, z<counter; i++)
				{
					if( cc[i] )
						p->c[kk][z++] = i+97;
				}  
			}
			else
			{
				p->k[kk] = 1;
				p->c[kk] = new char[1];
				p->c[kk][0] = t;
			} 
		}
        
        outputf<<"Case #"<<numN+1<<": "<<check(p,&root,0,L-1)<<endl;
        delete p;
	}
	
    outputf.close();
	inputf.close();
	
	root.~node();
	
	return 0;
}
