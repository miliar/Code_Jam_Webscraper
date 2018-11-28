#include <iostream>
#include <fstream>

using namespace std;
int gettime(ifstream &);
void sort(int [],int);

int main()
{
  int N,NA,NB,T;
  int NAst,NBst;
  int i,ia,ib;
  int hr,min;
  int depa[100],depb[100],pdepa[100],pdepb[100];
  ifstream ifile;
  ofstream ofile;
  ifile.open("B-large.in",ios_base::in);
  ofile.open("B-large.out",ios_base::out);
  ifile>>N;
  cout<<N<<endl;
  
  for(i=1;i<=N;i++)
  {
    ifile>>T>>NA>>NB;
    NAst=NA;
    NBst=NB;
    
    for(ia=0;ia<NA;ia++)
    {
      depa[ia]=gettime(ifile);
      pdepb[ia]=gettime(ifile)+T;
    }
    for(ib=0;ib<NB;ib++)
    {
      depb[ib]=gettime(ifile);
      pdepa[ib]=gettime(ifile)+T;
    }
    if(NA!=0 && NB!=0)
    {
      sort(depa,NA);
      sort(depb,NB);
      sort(pdepa,NB);
      sort(pdepb,NA);
      for(ia=ib=0;ib<NB && ia<NA;ib++)
	while(ia<NA)
	  if(depa[ia++]>=pdepa[ib])
	  {
	    NAst--;
	    break;
	  }
      for(ia=ib=0;ib<NB && ia<NA;ia++)
	while(ib<NB)
	  if(depb[ib++]>=pdepb[ia])
	  {
	    NBst--;
	    break;
	  }
    }
    ofile<<"Case #"<<i<<": "<<NAst<<" "<<NBst<<endl;
  }
  ifile.close();
  ofile.close();
  return 0;
}

int gettime(ifstream &fi)
{
  int hr=0,min=0;
  char c;
  do
  {
    fi.get(c);
  }while(c=='\n'||c=='\r'||c=='\t'||c==' ');
  //Get Hour.
  while(c!=':')
  {
    hr=hr*10+(c-'0');
    fi.get(c);
  }
  //Get Minutes.
  fi.get(c);
  while(c>='0' && c<='9' )
  {
    min=min*10+(c-'0');
    fi.get(c);
  }
  return hr*60+min;
}

void sort(int arr[],int n)
{
  int temp;
  for(int pop=n-1;pop>=1;pop--)
    for(int j=0;j<pop;j++)
      if(arr[j]>arr[j+1])
      {
	temp=arr[j];
	arr[j]=arr[j+1];
	arr[j+1]=temp;
      }
}
