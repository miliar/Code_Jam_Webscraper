#include<iostream>
#include<vector>
#include<fstream>
#include<map>
using namespace std;
ifstream fin("B-small-attempt0.IN");
ofstream fout("B-small-attempt0.OUT");
#define cin fin
#define cout fout

bool myfunction(pair<int,int> i,pair<int,int> j);
int decide(vector<pair<int,int> > vect1);
int main()
{
int rew;
cin >> rew;

for(int gf=0;gf<rew;gf++)
{
int x,y;
cin  >> x >> y;
int array[x][y];
int array1[x][y];
int count=1;
vector<int> sinks[27];
vector<pair<int,int> > vect1[x*y];
map<int,int> allpairs;
for(int q=0;q<x;q++)
for(int w=0;w<y;w++)
{
array[q][w]=count++;
}


for(int q=0;q<x;q++)
for(int w=0;w<y;w++)
{
cin >> array1[q][w];
pair<int,int> pairs(array1[q][w],0);
vect1[array[q][w]-1].push_back(pairs);
}



for(int q=0;q<x;q++)
{
for(int w=0;w<y;w++)
{

if(w>0)
{
pair<int,int> pairs(array1[q][w-1],array[q][w-1]);
vect1[array[q][w]-1].push_back(pairs);
//cout << "1" << endl;
}
if(w<(y-1))
{
pair<int,int> pairs(array1[q][w+1],array[q][w+1]);
vect1[array[q][w]-1].push_back(pairs);
//cout << "2" << endl;
}
if(q<(x-1))
{
pair<int,int> pairs(array1[q+1][w],array[q+1][w]);
vect1[array[q][w]-1].push_back(pairs);
//cout << "3" << endl;
}
if(q>0)
{
pair<int,int> pairs(array1[q-1][w],array[q-1][w]);
vect1[array[q][w]-1].push_back(pairs);
//cout << "4" << endl;
}
}
}
count=0;
for(int t=1;t<=x*y;t++)
{
//if(t==5) cout << "here" << endl;
int ret = decide(vect1[t-1]);
//cout << ret << " " << t << endl;
if(ret==0) ret = t;
allpairs[t]=ret;
if(ret == t )
{
sinks[0].push_back(ret);
count++;
}
}
//cout << count << " count"<<endl;
sort(sinks[0].begin(),sinks[0].end());
//cout << sinks[0].size() << " size " << endl;
for(int t=0;t<sinks[0].size();t++)
{
sinks[t+1].push_back(sinks[0][t]);
//cout << sinks[t+1][0];
}
//cout << endl;
for(int y1=0;y1<20;y1++)
{
for(int t=1;t<=x*y;t++)
{
int value = allpairs[t];
vector<int>::iterator it = sinks[1].begin();
it = find(sinks[1].begin(),sinks[1].end(),value);
if(it!= sinks[1].end())
{
it = sinks[1].begin();
it = find(sinks[1].begin(),sinks[1].end(),t);
if(it == sinks[1].end())
sinks[1].push_back(t);
}
it = sinks[2].begin();
it = find(sinks[2].begin(),sinks[2].end(),value);
if(it!= sinks[2].end())
{
it = sinks[2].begin();
it = find(sinks[2].begin(),sinks[2].end(),t);
if(it == sinks[2].end())
sinks[2].push_back(t);
}




}
if((sinks[1].size() + sinks[2].size()) == x*y  )
break;
}
//cout << sinks[1].size() + sinks[2].size() << endl;

/*
vector<int>::iterator it = sinks[1].begin();
while(it!=sinks[1].end())
{
cout << *it << " " ;
it++;
}
it = sinks[2].begin();
while(it!=sinks[2].end())
{
cout << *it << " " ;
it++;
}
*/
vector<int>::iterator it = sinks[1].begin();
it = find(sinks[1].begin(),sinks[1].end(),1);
if(it!=sinks[1].end())
{
vector<int> v = sinks[1];
sinks[1] = sinks[2];
sinks[2]  = v ;
}

cout << "Case #"  << gf+1 << ":"  << endl;

for(int a=0;a<x;a++)
{
for(int b=0;b<y;b++)
{
vector<int>::iterator it = sinks[1].begin();
it = find(sinks[1].begin(),sinks[1].end(),array[a][b]);
if(it!= sinks[1].end())
{
if(b==(y-1))
cout << "b";
else
cout << "b " ;
}
else
{
if(b== (y-1))
cout << "a";
else
cout << "a ";
}
}
cout << endl;
}
}

}
bool myfunction(pair<int,int> i,pair<int,int> j) {
    if( i.first < j.first ) return true;
    if( j.first < i.first ) return false;
    return i.second < j.second;
}

int decide(vector<pair<int,int> > vect1)
{
sort(vect1.begin(),vect1.end(),myfunction);
vector<pair<int,int> >::iterator it = vect1.begin();
//while(it!=vect1.end())
//{
//cout << it->first << " " << it->second << endl;
//it++;
//}
//cout << endl ;
//it = vect1.begin();
return it->second;
}
