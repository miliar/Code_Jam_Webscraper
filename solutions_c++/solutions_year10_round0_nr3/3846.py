#include <iostream>
#include <fstream>

using namespace std;


int main()

{
   // cout<<"main started";
char x;
int T, outermost, i, data, r, sum, cost, n, q, temp;
ifstream ifile;
ofstream ofile;
ofile.open("C-small.out");
ifile.open("C-small.in");
if(!ofile || !ifile)
{
    cout<<"error in file opening";}
cout<<"going to enter stuff from file";
ifile>>T;
cout<<T<<endl;
int t=T;//read T from file
int N, R, k, trips, capacity, n_grps;

for(outermost=0; outermost<t; outermost++)
{
//read R from file
//ifile>>x;
ifile>>R;
//ifile>>x;
ifile>>k;
//ifile>>x;
ifile>>N;
//ifile>>x;
trips=R;
//read k from file
capacity=k;
//read N from file
n_grps=N;
cout<<R<<endl<<k<<endl<<N;
int* group=new int[N];

if(group==NULL)
{
    cout<<"error in memory allocation";}

for(i=0; i<N; i++)
{
//read data from file
ifile>>data;
//ifile>>x;

group[i]=data;
}
for(i=0;i<N; i++)
{
    cout<<group[i];
    }
//group[0]=1;
//group[1]=4;
//group[2]=2;
//group[3]=1;
/////////////////array generatednode pointers
cout<<"just outside calc loop\n";
//group[N-1]->next=NULL;
cost=0;
for(r=0; r<trips; r++)
{
	sum=0;

	for(n=0; n<n_grps; n++)
		{
			//traverse the list to keep on adding till capacity is not exceeded
sum+=group[0];
            temp = group[0];
  if(sum>capacity)
			{
			    sum-=group[0];
			break;

			}

//shift the pointers of the current state
			for(q=0; q<N-1;q++ )
			{
			    group[q]=group[q+1];
			    }
            group[N-1]=temp;




		}//end inner calc loop


cost+=sum;



}//end outer calc loop

ofile<<"Case #"<<outermost+1<<": "<<cost<<endl;//write to a file

delete [] group;
}//end outermost
//ifile.close();
//ofile.close();
return 0;
}
