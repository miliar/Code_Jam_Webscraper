/*#include <iostream>
#include <string>

using namespace std;

void insert_sort(int A[], int n)
{
	if(n<=1)
		return;
	insert_sort(A,n-1);
	
	int key=A[n-1];
	int j;
	for(j=n-2;j>=0;j--){
		if(A[j]<=key)
			break;
		A[j+1]=A[j];
	}
	A[j+1]=key;
	for(int i=0;i<n;i++)
		cout<<A[i]<<" ";
	cout<<endl;
}

main()
{
	int n=5;
	int *A;
	A=new int[n];
	A[0]=5;
	A[1]=2;
	A[2]=3;
	A[3]=10;
	A[4]=8;
	insert_sort(A,n);

	for(int i=0;i<n;i++)
		cout<<A[i]<<" ";
}

void LCS(char* x, char* y, int m, int n)
{
	int c[8][7];
	for(int i=1;i<=m;i++)
		c[i][0]=0;
	for(int j=0;j<=n;j++)
		c[0][j]=0;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
		{
			if(x[i]==y[j])
			{
				c[i+1][j+1]=c[i][j]+1;
			}
			else if(c[i][j+1]>=c[i+1][j])
			{
				c[i+1][j+1]=c[i][j+1];
			}
			else
			{
				c[i+1][j+1]=c[i+1][j];
			}
		}
	for(int i=1;i<=m;i++){
		for(int j=1;j<=n;j++)
			cout<<c[i][j];
		cout<<endl;
	}
}

main()
{
	char* y="BDCABA";
	char* x="ABCBDAB";
	LCS(x,y,7,6);
}

#define inf 100000

void Merge(int *A, int p, int q, int r)
{
	int n1=q-p+1;
	int n2=r-q;
	int *L;
	L=new int[r];
	int *R;
	R=new int[r];
	for(int i=1;i<=n1;i++)
		L[i]=A[p+i-1];
	for(int j=1;j<=n2;j++)
		R[j]=A[q+j];
	L[n1+1]=inf;
	R[n2+1]=inf;
	i=1;
	j=1;
	for(int k=p; k<=r;k++)
		if(L[i]<=R[j])
		{
			A[k]=L[i];
			i++;
		}
		else
		{
			A[k]=R[j];
			j++;
		}

}


void Merge_sort(int *A, int p, int r)
{
	if(p<r)
	{
		int q=(p+r)/2;
		Merge_sort(A,p,q);
		Merge_sort(A,q+1,r);
		Merge(A,p,q,r);
	}
}


main()
{
	int A[10]={3,2,9,5,7,11,8,23,10,4};
	Merge_sort(A,1,9);
	
	for(int i=1;i<=9;i++)
		cout<<A[i]<<endl;
}

void Greedy_Activity_Selector(int s[], int f[], int n)
{
	int A[10];
	A[0]=s[0];
	int flag=1;
	int k=0;
	for(int m=1;m<n;m++)
	{
		if(s[m]>=f[k])
		{
			A[flag++]=m;
			k=m;
		}
	}

	for(int i=0;i<n;i++)
		cout<<A[i]<<endl;
}

main()
{
	int s[]={1,3,0,5};
	int f[]={4,5,6,7};
	Greedy_Activity_Selector(s,f,4);
}*/

/*
#include <iostream>
#include <stdio.h>
#include <string>
#include <queue>
#include <stack>
using namespace std;

class Node{
	private:
		int data;
		Node* left;
		Node* right;
	public:
		string path;
		Node(int d){data=d; left=right=NULL; path="0";}
		Node(int d, Node* childleft, Node* childright){data=d; left=childleft;right=childright;path="0";}
		int getData(){return data;}
		Node* getLeft(){return left;}
		Node* getRight(){return right;}
};

class cmp{
public:
	bool operator()(Node* a, Node* b)
	{
		return a->getData()>=b->getData();
	}
};

void print(Node* a)
{
	if(a!=NULL)
	{
		cout<<(a->getData())<<endl;
		print(a->getLeft());
		print(a->getRight());
	}
}

int getDepth(Node* n)
{
	if (n==NULL)
		return 0;
	else
		return getDepth(n->getLeft())>getDepth(n->getRight())?getDepth(n->getLeft())+1:getDepth(n->getRight())+1;

}

void dfs(Node* n)
{
	stack<Node*> s;
	Node* ncopy=n;
	while(!s.empty()||ncopy!=NULL)
	{
		while(ncopy!=NULL)
		{
			cout<<ncopy->getData()<<endl;
			s.push(ncopy);
			ncopy=ncopy->getLeft();
		}
		if(!s.empty())
		{
			ncopy=s.top();
			s.pop();
			ncopy=ncopy->getRight();
		}
	}
}

void findsum(Node* n, int sum, stack<int> s)
{
	if(n==NULL)
		return;
	s.push(n->getData());
	if(n->getLeft()==NULL&&n->getRight()==NULL)
	{
		if(n->getData()==sum)
		{
			stack<int> stemp;
			while(s.size()>0)
			{
				stemp.push(s.top());
				s.pop();
			}
			while(stemp.size()>0)
			{
				cout<<stemp.top()<<endl;
				s.push(stemp.top());
				stemp.pop();
			}
		}
	}
	findsum(n->getLeft(),sum-n->getData(),s);
	findsum(n->getRight(),sum-n->getData(),s);
}

main()
{
	Node* m1=new Node(3,NULL,NULL);
	Node* m2=new Node(4,NULL,NULL);
	Node* m3=new Node(5,m1,m2);
	Node* m4=new Node(10,NULL,NULL);
	Node* m5=new Node(14,m4,NULL);

	Node* root=new Node(2,m3,m5);

	queue<Node*> q;
	q.push(root);
	while(q.size()>0)// print node via BFS
	{
		cout<<q.front()->getData()<<endl;
		if(q.front()->getLeft()!=NULL)
		{
			q.push(q.front()->getLeft());
			q.front()->getLeft()->path=q.front()->path+"0";
		}
		if(q.front()->getRight()!=NULL)
		{
			q.push(q.front()->getRight());
			q.front()->getRight()->path=q.front()->path+"1";
		}
		cout<<"*"<<q.size()<<endl;
		q.pop();
		cout<<"#"<<q.size()<<endl;
	}

	cout<<endl<<getDepth(root)<<endl<<endl;//check tree balance
	if(abs(getDepth(root->getLeft())-getDepth(root->getRight()))>1)
		cout<<"not balance"<<endl;
	else
		cout<<"balance"<<endl;

	print(root);//pre-order print


	int key1=3,key2=10;//nearest common father node
	string k1,k2;
	queue<Node*> q2;
	q2.push(root);
	while(q2.size()>0)
	{
		if(q2.front()->getLeft()!=NULL)
		{
			q2.push(q2.front()->getLeft());
		}
		if(q2.front()->getRight()!=NULL)
		{
			q2.push(q2.front()->getRight());
		}
		if(q2.front()->getData()==key1)
			k1=q2.front()->path;
		else if(q2.front()->getData()==key2)
			k2=q2.front()->path;

		q2.pop();
	}
	for(int i=0;i<k1.length()&&i<k2.length()&&k1[i]==k2[i];i++)
		cout<<k1[i]<<endl;
	cout<<k1<<endl;
	cout<<k2<<endl<<"**"<<endl;

	dfs(root);//dfs
	cout<<endl;

	stack<int> s;//find sum of keys along a path equals to a number 
	findsum(root,26,s);
	cout<<endl;

	int array[]={1,2,4,8,15};
	priority_queue<Node*,vector<Node*>,cmp> pq;
	for(int i=0;i<5;i++)
		pq.push(new Node(array[i]));
	while(pq.size()>1)
	{
		Node* a1=pq.top();
		pq.pop();
		Node* a2=pq.top();
		pq.pop();
		pq.push(new Node(a1->getData()+a2->getData(),a1,a2));
	}
	Node* nroot=pq.top();
	print(nroot);

}
*/

/*
#include <iostream>
#include <string>
#include <stdio.h>
#include <time.h>
using namespace std;

main()
{
	int a[]={3,	4,	9,	14,	15,	19,	28,	37,	47,	50,	54,	56,	59,	61,	70,	73,	78,	81,	92,	95,	97,	99};
	int b[100]={0};
	b[3]=b[4]=b[9]=b[14]=b[15]=b[19]=b[28]=b[37]=b[47]=b[50]=b[54]=b[56]=b[59]=b[61]=b[70]=b[73]=b[78]=b[81]=b[92]=b[95]=b[97]=b[99]=1;
	int sum=0;

	clock_t start,end;
	start=clock();
	for(int i=0;i<22;i++)
	{
        for(int j=0;j<100;j++)
		{
			if(b[j]>=1&&j>=a[i])
				b[j-a[i]]+=b[j];
		}
	}
	end=clock();
	for(int i=0;i<100;i++)
		if(b[i]>0)
			cout<<i<<" "<<b[i]<<endl;
	cout<<"time"<<(double)(end - start) / CLOCKS_PER_SEC<<endl;

}*/

/*
#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

string reString(string s)
{
	if(s.length()<=1)
		return s;
	string left=s.substr(0,s.length()/2);
	string right=s.substr(s.length()/2,s.length()-1);
	return reString(right)+reString(left);	
}

string revS(string s)
{
	if(s.length()<=1)
		return s;
	return s[s.length()-1]+revS(s.substr(1,s.length()-2))+s[0];
}

int c[1170][1170];

void LCS(string x, string y, int m, int n)
{
	for(int i=1;i<=m;i++)
		c[i][0]=0;
	for(int j=0;j<=n;j++)
		c[0][j]=0;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
		{
			if(x[i]==y[j])
			{
				c[i+1][j+1]=c[i][j]+1;
			}
			else
			{
				c[i+1][j+1]=0;
			}
		}
	int lar=0;
	int position[2];
	for(int i=1;i<=m;i++)
		for(int j=1;j<=n;j++)
			if(c[i][j]>lar){
				lar=c[i][j];
				position[0]=i;
				position[1]=j;
			}
	cout<<position[0]<<" "<<position[1]<<" "<<lar<<endl;
	cout<<endl;
}

main()
{
	//string s="Ilikeracecarsthatgofast";
	string S="FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
	cout<<revS(S)<<endl;

	cout<<S.substr(204,7)<<endl;
	LCS(s,revS(s),s.length(),s.length());
}*/


/*
#include <iostream>
#include <string>

using namespace std;

class line{
public:
	double slope;
	double yintercept;
	line(double s, double intercept){slope=s; yintercept=intercept;}
	bool cross(line l){ 
		if(slope==l.slope&&yintercept!=l.yintercept)
			return false;
		else
			return true;
	}
};

main()
{
	line l1(1,2);
	line l2(1,3);
	cout<<l1.cross(l2)<<endl;
}*/

/*
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int prime_factor(int n, vector<int> &fact)
{
  for(int j=2;j<=n;j++)
  {
    int jcopy=j;
	int i=2;
	while(i<=sqrt(double(j)))
	{
		for(;i<=sqrt(double(j));i++)
			if(j%i==0)
			{
				j=j/i;
				fact[i]++;
				cout<<i<<'*'<<endl;
				break;
			}
	}
	cout<<j<<endl<<endl;
	fact[j]++;
	j=jcopy;
  }

  return 0;
}

main()
{
	vector<int> fact;
	fact.assign(100,0);
	int n;
	cin>>n;
	prime_factor(n,fact);

	cout<<"2:"<<fact[2]<<" 5:"<<fact[5]<<endl;
}*/


/*
    #include <iostream>  
    using namespace std ;  
      
    #define N  64  
      
    void compute_change(int c[],int n ,int d[] ,int k,int a[])   
    {  
        for(int j=1 ; j<=n ; j++)  
        {  
           c[j]=j;  
           for(int i=1 ; i<=k ; i++)  
           {  
               if(j>=d[i] && (1+c[j-d[i]]) < c[j])  
               {  
                   c[j]=1+c[j-d[i]] ;  
                   a[j]=d[i];  
               }  
           }  
       }  
   }  
     
   void give_change(int a[],int j)  
   {  
       if(j>0)  
           cout<<"找零钱:"<<a[j]<<endl;  
       give_change(a,j-a[j]);  
   }  
     
   int main()  
   {  
       int d[]={0 , 25 , 10 ,  1} ;  
       int c[N]={0} ;  
       int a[N]={0};//记录找每个N分钱时最优的di值  
     
       compute_change(c,30,d,3,a) ;  
       cout << "最优解就是最少值为：" << c[30] << endl ;  
       give_change(a,30);  
     
   }  
   
*/

/*
#include <iostream>
#include <string>
using namespace std;

int modify_fab(int start, int n)
{
	if (n==1||n==2)
		return start;
	else
		return modify_fab(start,n-1)+modify_fab(start,n-2);

}

main()
{
	int start,end;
	cin>>start;
	cin>>end;
	for(int i=1; ;i++)
	{
		int temp=modify_fab(start,i);
		if(temp>end)
			return;
		else
			cout<<temp<<endl;
	}


}*/

/*
#include<iostream>
#include<string>
#include<stdio.h>
#include<sstream>
using namespace std;

string reverse(string s)
{
	if (s.length()<=1)
		return s;
	else
		return s[s.length()-1]+reverse(s.substr(1,s.length()-2))+s[0];
}

bool isleap(int y)
{
	if(y%400==0||(y%100!=0&&y%4==0))
		return 1;
	else
		return 0;	
}

main()
{
	//string s="hello world";
	//cout<<reverse(s)<<endl;
	int start, end;
	int map[]={31,28,31,30,31,30,31,31,30,31,30,31};
	
	start=202;
	end=2010;
	stringstream s1;


	for(int i=start;i<=end;i++)
		for(int j=1;j<=12;j++)
			for(int k=1;k<=map[j];k++)
			{
				s1.str("");
				if (j<10)
					s1<<"0"<<j;
				else
					s1<<j;
				string s=s1.str();
				s1.str("");
				if (k<10)
					s1<<"0"<<k;
				else
					s1<<k;
				s=s+s1.str();
				s1.str("");
				s1<<i;
				s=s+s1.str();
				
				//cout<<s<<endl;
				
				string reverse_s=reverse(s);
				if(s.compare(reverse_s)==0)
					cout<<s<<endl;
			}

	cout<<"end"<<endl;
	return;
}
*/

/*
#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>

using namespace std;

string rev(string s)
{
	if(s.length()<=1)
		return s;
	else
		return rev(s.substr(s.length()/2,s.length()-s.length()/2))+rev(s.substr(0,s.length()/2));
}

bool isleapyear(int year)
{
	if(year%400==0||(year%100!=0&&year%4==0))
		return true;
	else
		return false;
}

main()
{
	string start;
	string end;
	int date[6];
	cin>>start;
	cin>>end;
	date[0]=atoi((start.substr(0,2)).c_str());
	date[1]=atoi((start.substr(2,2)).c_str());
	date[2]=atoi((start.substr(4,4)).c_str());
	date[3]=atoi((end.substr(0,2)).c_str());	
	date[4]=atoi((end.substr(2,2)).c_str());
	date[5]=atoi((end.substr(4,4)).c_str());	

		
	int month[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
	int month2[]={0,31,29,31,30,31,30,31,31,30,31,30,31};
	
	for(int i=date[2];i<=date[5];i++)
		for(int j=1,k=1;j<=12;j++,k=1)
		{
			if(i==date[2]&&j<=date[0])
			{
				j=date[0];
				k=date[1];
			}
			if(i==date[5]&&j==date[3])
			{
				month[j]=date[4];
				month2[j]=date[4];
				j=12;
			}

			if(isleapyear(i))
			{
				for( ;k<=month2[j];k++)
				{
					stringstream ss;
					string tim;
					if(j<10)
						ss<<"0"<<j;
					else
						ss<<j;
					if(k<10)
						ss<<"0"<<k;
					else
						ss<<k;
					ss<<i;
					tim=ss.str();
					if(tim.compare(rev(tim))==0)
						cout<<tim<<endl;
				}
			}
			else
			{
				for( ;k<=month[j];k++)
				{
					stringstream ss;
					string tim;
					if(j<10)
						ss<<"0"<<j;
					else
						ss<<j;
					if(k<10)
						ss<<"0"<<k;
					else
						ss<<k;
					ss<<i;
					tim=ss.str();
					if(tim.compare(rev(tim))==0)
						cout<<tim<<endl;
				}
			}
		}
	cout<<"jk"<<endl;
	return 0;
	
}
*/


/*
#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
using namespace std;

main()
{
	int in[4][4]={0};
	int count=1;
	for(int i=1;i<=3;i++)
		for(int j=1;j<=3;j++)
		{
			in[i][j]=count++;
		}
	
	int sign[10][10];
	sign[1][in[1][2]]=sign[1][in[2][1]]=1;
	sign[2][in[1][1]]=sign[2][in[1][3]]=sign[2][in[2][2]]=1;
	sign[3][in[1][2]]=sign[3][in[2][3]]=1;
	sign[4][in[1][1]]=sign[4][in[2][2]]=1;
	sign[5][in[1][2]]=sign[5][in[2][1]]=sign[5][in[2][3]]=sign[5][in[3][2]]=1;
	sign[6][in[1][3]]=sign[6][in[2][2]]=sign[6][in[3][3]]=1;
	sign[7][in[2][1]]=sign[7][in[3][2]]=1;
	sign[8][in[2][2]]=sign[8][in[3][1]]=sign[8][in[3][3]]=1;
	sign[9][in[2][3]]=sign[9][in[3][2]]=1;

	string key;
	string enter;
	int error=0;
	cin>>key;
	cin>>enter;
	for(int i=0;i<min(key.length(),enter.length());i++)
	{	
		if(key[i]==enter[i])
			;
		else
		{
			int k1=atoi(key.substr(i,1).c_str());
			int e1=atoi(enter.substr(i,1).c_str());
			if(sign[k1][e1]==1)
				;
			else
				error++;
		}
	}
	error+=abs((int)enter.length()-(int)key.length());
	if(error==0)
		cout<<"OK"<<endl;
	else
		cout<<"Not Right"<<endl;

}
*/

/*
#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

main()
{
	double basewage;
	cin>>basewage;
	double N;
	cin>>N;
	char character;
	cin>>character;
	
	if(N<1)
		return false;
	if(basewage*(3+6*N*0.01)>50000)
		return false;
	
	if(character=='A')
		cout<<basewage*(1+N*0.01)<<endl;
	else if(character=='B')
		cout<<basewage*(1+N*0.02)<<endl;
	else if(character=='C')
		cout<<basewage*(1+N*0.03)<<endl;

	cout<<"kk"<<endl;
}
*/


/*
#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

main()
{
	int odd;
	int even;
	int flag1=0;
	int flag2=0;
	int enter;

	while(cin>>enter)
	{
		if(enter==0)
			break;
		if(enter%2==0)
		{
			if(flag2==0)
			{
				even=enter;
				flag2++;
			}
			else
			{
				even=enter<even?enter:even;
			}
		}
		else if(enter%2==1)
		{
			if(flag1==0)
			{
				odd=enter;
				flag1++;
			}
			else
			{
				odd=enter>odd?enter:odd;
			}
		}

	}
	cout<<odd<<" "<<even<<endl;
	cout<<"kl"<<endl;
}
*/


/*
#include <iostream>
#include <string>
#include <stdio.h>
#include <sstream>
using namespace std;

void light(int a, int b, FILE *fp)
{
	string s="";
	while(b>0)
	{
		int t=b%2;
		stringstream ss;
		ss<<t;
		b=b/2;
		s=s+ss.str();
	}
	if(s[a-1]=='1')
		fprintf(fp,"ON\n");
	else
		fprintf(fp,"OFF\n");
}

main()
{
	FILE *fp;
	fp=fopen("C:\\Documents and Settings\\yunzhang\\桌面\\A.txt","r");
	if(fp==NULL)
		cout<<"error"<<endl;
	char c;
	int num;
	int a[10000][2];
	int count=0;
	string out;
	fscanf(fp,"%d%c",&num,&c);
	while(count<num)
	{
		fscanf(fp,"%d%c%d%c",&a[count][0],&c,&a[count][1],&c);
		count++;
	}
	fclose(fp);

	fp=fopen("C:\\Documents and Settings\\yunzhang\\桌面\\light.txt","w");
	for(int i=0;i<num;i++)
	{
		fprintf(fp,"Case #%d: ",i+1);
		light(a[i][0],a[i][1],fp);
	}
	fflush(fp);
	fclose(fp);
	cout<<"ll"<<endl;
}
*/


/*
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;


int add(int a,int b)
{
	if(a==0)
		return b;
	else if(b==0)
		return a;
	int sum=a^b;
	int carry=(a&b)<<1;
	return add(sum,carry);	
}

main()
{
	cout<<add(7,14)<<endl;
}
*/

/*
#include <iostream>
#include <conio.h>
using namespace std;

int swapbits(int x)
{
	int a=(x&0xaaaaaaaa) >>1;
	int b=(x&0x55555555) <<1;
	return ( ((x&0xaaaaaaaa) >>1) | (( x&0x55555555) <<1));
}

main()
{
	cout<<swapbits(0x9)<<endl;
	cout<<swapbits(0x5)<<endl;
	_getch();
}
*/

/*
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

main()
{
	FILE *fp;
	fp=fopen("C:\\Documents and Settings\\yunzhang\\桌面\\A.txt","r");
	if(fp==NULL)
		cout<<"error"<<endl;
	FILE *fp1;
	fp1=fopen("C:\\Documents and Settings\\yunzhang\\桌面\\O.txt","w");
	int number;
	fscanf(fp,"%d",&number);
	int count=1;
	while(number>0)
	{
		int n;
		char c;
		int a[1000];
		fscanf(fp,"%d",&n);
		int index=0;
		int sum=0;
		while(index<n)
		{
			fscanf(fp,"%d%c",&a[index],&c);
			sum=sum^a[index];
			index++;
		}
		if(sum!=0)
		{
			cout<<"Case #"<<count<<": "<<"NO"<<endl;
			fprintf(fp1,"Case #%d: NO\n",count);
		}
		else
		{
			int min=a[0];
			int tsum=0;
			for(int i=0;i<n;i++)
			{
				tsum+=a[i];
				if(a[i]<min)
					min=a[i];
			}
			cout<<"Case #"<<count<<": "<<tsum-min<<endl;
			fprintf(fp1,"Case #%d: %d\n",count,tsum-min);
		}
		number--;
		count++;
	}
	fflush(fp1);
	fclose(fp);
	fclose(fp1);
}
*/

#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

bool isint(float x)
{
	return ((x)-(int)(x)<0.0001?1:0);
}

main()
{
	FILE *fp;
	fp=fopen("C:\\Documents and Settings\\yunzhang\\桌面\\B.txt","r");
	if(fp==NULL)
		cout<<"error"<<endl;
	FILE *fp1;
	fp1=fopen("C:\\Documents and Settings\\yunzhang\\桌面\\Out.txt","w");
	int number;
	fscanf(fp,"%d",&number);
	int count=1;

	while(number>0)
	{
		char N[20];
		int pd,pg;
		char c,c1;
		int win=-1;
		fscanf(fp,"%s%c%d%c%d",N,&c,&pd,&c1,&pg);
		int len=strlen(N);
		if((pd>0&&pg==0)||(pd<100&&pg==100))
			fprintf(fp1,"Case #%d: Broken\n",count);
		else if(len>2)
			fprintf(fp1,"Case #%d: Possible\n",count);			
		else
		{
			int n=atoi(N);
			for(int i=n;i>0;i--)
			{
				float t=i*pd/100.0;
				if(isint(t)){
					win=(int)t;
					break;
				}
			}
			if(win!=-1)
                fprintf(fp1,"Case #%d: Possible\n",count);
			else
				fprintf(fp1,"Case #%d: Broken\n",count);
		}
		number--;
		count++;
	}
	fflush(fp1);
	fclose(fp);
	fclose(fp1);
}