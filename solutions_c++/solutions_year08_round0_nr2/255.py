#include <iostream>
#include <set>
#include <map>
using namespace std;

int gettime()
{
  int h,m;
  char dmy;
  cin>>h>>dmy>>m;
  return h*60+m;
}

int main()
{
  int cases;cin>>cases;
  for (int c=1;c<=cases;c++){
    int t;cin>>t;
    int na,nb;cin>>na>>nb;

    multiset<pair<int,pair<int,int> > > mm;

    for (int i=0;i<na;i++){
      int st=gettime();
      int ed=gettime();
      mm.insert(make_pair(st,make_pair(1,0)));
      mm.insert(make_pair(ed+t,make_pair(0,1)));
    }
    for (int i=0;i<nb;i++){
      int st=gettime();
      int ed=gettime();
      mm.insert(make_pair(st,make_pair(1,1)));
      mm.insert(make_pair(ed+t,make_pair(0,0)));
    }

    int tra[2]={0};
    int sta[2]={0};

    for (multiset<pair<int,pair<int,int> > >::iterator p=mm.begin();
	 p!=mm.end();p++){
      int arr=p->second.first;
      int pla=p->second.second;

      //cout<<p->first<<": "<<pla<<" "<<arr<<endl;

      if (arr==0){
	tra[pla]++;
      }
      else{
	if (tra[pla]>0) tra[pla]--;
	else sta[pla]++;
      }
    }

    cout<<"Case #"<<c<<": "<<sta[0]<<" "<<sta[1]<<endl;
  }
  return 0;
}
