/*
 *  main.cpp
 *  
 *
 *  Created by Mayank Jaiswal on 03/09/09.
 *  Copyright 2009 IIT Kharagpur. All rights reserved.
 *
 */


#include <iostream>
#include <algorithm>
#define DEBUG false
int D;

using namespace std;




void sort_words(char *x[], int y) {
  int i = 0;
  int j = 0;
  
  for(i = 0; i < y; ++i)
	for(j = i + 1; j < y; ++j)
	  if(strcmp(x[i], x[j]) > 0)
		swap(x[i], x[j]);
}

void swap(char *p, char *q) {
  char *tmp;
  
  tmp = p;
  p = q;
  q = tmp;
}






class Reply
  {
  public:
	bool b;
	int ptr;
	Reply(bool bx ,  int ptrx)
	{
	  b=bx;
	  ptr=ptrx;
	}
  };


class Testcase
  {
  public: 
	int L;
	int count;//count of number of combinations
	int *p;// pointer array ro generate combinations
	char *s;
	char **W;
	char str[500];
	char **letters;
	char ** words;

	Testcase(int Lx, char  ** Wx);
	int solve(int a);
	void print();
	void increment_p();
	void print_p();
	Reply isAvailable(char * in_str, int start);
  };


Testcase :: Testcase (int Lx, char ** Wx)
{
  L=Lx;
  W=Wx;
  cin >> str;
  letters = new char * [L];
  
  int ptr=0;
  
  for(int i=0 ;i < L ;i++,ptr++)
  {
	letters[i] =new char [30];
	if(str[ptr]=='(')
	{
	  ptr++;
	  int j=0;
	  for( j=0;str[ptr] !=')';j++, ptr++)
	  {
		letters[i][j]=str[ptr];
	  }
	  letters[i][j]='\0';
	  sort(letters[i],letters[i]+strlen(letters[i]));
	}
	else
	{
	  letters[i] =new char [30];
	  letters[i][0]=str[ptr];
	  letters[i][1]='\0';
	  
	}
	
	
	
	
	
  }
  
}





void Testcase :: increment_p()
{

  
  for(int i=L-1 ;i >=0  ;i--)
  {
	if(p[i]<strlen(letters[i])-1)
	{ 
	  p[i]++;
	  break;
	}
	else
	  p[i]=0;
  }
  

}


void Testcase :: print()
{
  cout<< "\t";
  for(int i=0 ;i < L ;i++)
  {
	cout << letters[i] << " "; 
  }
  cout << endl;
  
  //cout<<"\t\t"<< str << endl;
  
}




void Testcase ::print_p()
{
  cout << "Pointer p: ";
  for(int i=0 ;i < L ;i++)
	cout<< p[i]<< " ";
	
  cout << endl;
}

Reply Testcase ::isAvailable(char * in_str, int start)
{
  int i;
  for( i=start ;i < D ;i++)
  {
	int flag=0;
	
	if(strcmp(in_str, W[i])< 0)
	{
	  flag=1;
	  cout <<"\tThats it!   "<<W[i] <<">"<<in_str<<endl ;
	  return Reply(false,i-1);
	}
	else if(strcmp(in_str, W[i])> 0)
	{
	  flag=-1;
	  cout <<"\tX   "<<W[i] <<endl ;
	  cout <<"\tHurray   W[i]"<<W[i] <<"<"<<in_str<<"(in_str)  ....."<< W[i]<<" willnot be checked now!"<<endl ;

	  break;
	}
	else
	  return Reply(true,i);
  }  

  
  //this is executed when in_str > W[i]
  
  while(strcmp(in_str, W[i])> 0 && i<D)
  {
	i++;
	if(i==D) break;
  }
  
  
  cout <<"\tHurray   "<<W[i] <<">"<<in_str<<".....Uptil "<< W[i]<<" willnot be checked now!"<<endl ;
  return Reply(false,i);  

  cout << "value of i sent ="<< i<<endl; 
  
  
  
}




int main ()
{
  int L;
  int N;
  
  cin>>L;
  cin>>D;
  cin>>N;
  
  if (DEBUG) cout << "Parameters:" << endl;
  if (DEBUG) cout << "\tL=" << L<<endl;
  if (DEBUG) cout << "\tD=" << D<<endl;
  if (DEBUG) cout << "\tN=" << N<<endl;
  
  
  char ** words;
  words =new char * [D];
  
  for(int i=0; i<D ;i++ )
  {
	words[i]= new char [L+1];
	
	for(int j=0; j<=L ; j++)
	{
	  if(j==L)
		words[i][j]='\0';
	  else
		cin >> words[i][j];
	}
  }
  
  sort_words(words,D);
  
  
  if (DEBUG) cout << "Available words:" << endl;
  for(int i=0; i<D ;i++ )
  {
	if (DEBUG) cout<< "\t" << words[i]<< endl;
  }
  
  Testcase **T;
  T= new Testcase *[N];
  
  //Reading Testcases
  for(int i=0; i<N ;i++ )
	T[i] = new Testcase(L,words);
  
  //printing this testcase
  if (DEBUG) cout << "Testcases: "<<endl;
  for(int i=0; i<N ;i++ )
	if (DEBUG) T[i]->print();
  
  
  
  
  int result[N];
  for(int i=0; i<N ;i++ )
	result[i] = T[i]->solve(i+1);  
  
  for(int i=0; i<N ;i++ )
	cout<< "Case #"<<i+1 << ": "<<result[i]<< endl;
  
  
  
  return 0;
}



bool isThere( char c , char* arr )
{
  
  for(int j=0; j< strlen(arr) ; j++)
  {
	if(c==arr[j])
	  return true;
  }
  return false;
  
}



int Testcase :: solve(int testno)
{
  if (DEBUG)  cout << "\n\nSolving testcase no : "<<testno<<endl; 
  //Calculating count
  //count=1;
 // 
//  for(int i=0; i< L; i++)
//  {
//	count *= strlen(letters[i]);
//	cout<<strlen(letters[i])<< " * " ;
//  }
//  if (DEBUG)  cout << "count ="<<count<<endl;
//  
  int res=0;
  for(int ptr=0 ;ptr < D ;ptr++) 
  {
	int flag=1;
	for(int i=0; i< L; i++) // i moves on W[ptr]
	{
	  if(!   isThere(W[ptr][i],letters[i])   ) 
	  {
		
		flag=0;
		break;
	  }
	}
	if(flag==1)
	  res++;
  }
  
  //cout<<" ######## "<< res<<" ##########"<<endl;
  return res; 
}


//Initialize pointer
//  p= new int [L];
//  //print_p();
//  // increment_p();
//  //  print_p();
//  //  increment_p();
//  //  print_p();
//  //  increment_p();
//  //  print_p();
//  //  increment_p();
//  
//  
//  //words=new char*[count];
//  //  int ptr[L];
//  s = new char [L+1]; 
//  int result=0;
//  int start=0;
//  for(int  c=0; c< count; c++)
//  {
//	for(int  i=0; i< L; i++)
//	  s[i]=letters[i][p[i]];
//	s[L]='\0';
//	if (DEBUG)print_p();
//	if (DEBUG)cout<< "s: " << s<<endl;
//	Reply rep=isAvailable(s,start);
//	if(rep.b==true) 
//	{
//	  result++;
//	  start=rep.ptr+1;
//	}
//	else if(rep.b==false)
//	{
//	  if(rep.ptr==start)
//		;//do nothing
//	  if(rep.ptr==D)
//		break;//do nothing
//	  else
//		start=rep.ptr+1;
//	  cout<< "From solve() : {start,D} =   "<< start<<","<< D<<endl;
//	}
//	
//	
//	
//	
//	
//	
//	//if (DEBUG)cout<< b<<endl;
//	
//	increment_p();  
//	if(start>=count)
//	  break;
//	
//  }
//  
//  return result;






