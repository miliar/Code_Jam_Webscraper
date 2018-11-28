#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int key=0;

vector<pair<double,double> > solve(double length,double width,const vector<pair<double,int> >& circle);

int main(){
  int t;
  cin>>t;
  cout.setf(ios::fixed|ios::showpoint);
  cout.precision(6);
  for(int i=0;i<t;i++){
    int circles,length,width;
    cin>>circles>>length>>width;
    vector<pair<double,int> > circle(circles);
    for(int j=0;j<circles;j++){
      cin>>circle[j].first;
      circle[j].second=j;
    }
    bool swapped=false;
    if(length<width){
      swap(length,width);
      swapped=true;
    }
    sort(circle.begin(),circle.end());
    reverse(circle.begin(),circle.end());
    vector<pair<double,double> > position=solve(length,width,circle);
    cout<<"Case #"<<i+1<<':';
    for(int i=0;i<circle.size();i++){
      if(swapped)
        swap(position[i].first,position[i].second);
      cout<<' '<<position[i].first<<' '<<position[i].second;
    }
    cout<<'\n';
  }
}

void place(const double length,const double width,const double x,const double y,const vector<pair<double,int> >& circle,vector<pair<double,double> >& position,vector<bool>& placed,bool top,bool left){
  for(int i=0;i<circle.size();i++){
    const double radius=circle[i].first;
    if(placed[i])
      continue;

    const double diameter=2*radius;
    double place_length=top?radius:diameter;
    double place_width=left?radius:diameter;
    double place_dx=top?0:radius;
    double place_dy=left?0:radius;
    double place_x=x+place_dx;
    double place_y=y+place_dy;

    if(!top && place_dx+radius>length)
      continue;

    if(!left && place_dy+radius>width)
      continue;

    //cout<<"placing in "<<length<<','<<width<<" of "<<circle[i].second<<" at "<<x<<','<<y<<" "<<top<<','<<left<<'\n';

    position[circle[i].second]=make_pair(place_x,place_y);
    placed[i]=true;

    if(width>place_width)
      place(place_length,width-place_width,x,y+place_width,circle,position,placed,top,false);
    if(length>diameter)
      place(length-place_length,width,x+place_length,y,circle,position,placed,false,left);
    return;
  }
}

const double epsilon=1e-3;

bool overlap(double x,double r,double xx,double rr){
  if(x+r < xx-rr+epsilon)
    return false;
  if(xx+rr < x-r+epsilon)
    return false;
  return true;
}

vector<pair<double,double> > solve(double length,double width,const vector<pair<double,int> >& circle){
  vector<pair<double,double> > position(circle.size());
  vector<bool> placed(circle.size(),false);
  place(length,width,0,0,circle,position,placed,true,true);
  for(int i=0;i<circle.size();i++){
    assert(placed[i]);
    int c=circle[i].second;
    assert(0<=position[c].first && position[c].first<=length);
    assert(0<=position[c].second && position[c].second<=width);
  }

  for(int i=0;i<circle.size();i++)
    for(int j=i+1;j<circle.size();j++){
    int a=circle[i].second,b=circle[j].second;
    double ax=position[a].first,ay=position[a].second,ar=circle[i].first;
    double bx=position[b].first,by=position[b].second,br=circle[j].first;
    if(overlap(ax,ar,bx,br) && overlap(ay,ar,by,br)){
      cout<<a<<" overlaps with "<<b<<'\n';
      cout<<ax<<','<<ay<<" of "<<ar<<' '<<ax-ar<<'-'<<ax+ar<<" & "<<ay-ar<<'-'<<ay+ar<<'\n';
      cout<<bx<<','<<by<<" of "<<br<<' '<<bx-br<<'-'<<bx+br<<" & "<<by-br<<'-'<<by+br<<'\n';
      assert(false);
    }
  }
  return position;
}
