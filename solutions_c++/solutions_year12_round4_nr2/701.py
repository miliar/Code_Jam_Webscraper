#include<iostream>
#include<cstdio>
#include<iomanip>
#include<cassert>
#include<algorithm>
#include<vector>
#include<utility>

using namespace std;

vector<int> ri;
int w;
int h;

int n;
vector<pair<int,int> > sr;
double pos_x[2000];
double pos_y[2000];
struct btree{

    btree* up, *down;
    bool full;
    double x0,y0,x1,y1;
    double w(){
        return x1-x0;
    }
    double h(){
        return y1-y0;
    }
    bool axis(){
        return w()>h();
    }
    btree(){
        up = down = 0;
        full = false;
    }
    bool w_up(){
        return y0==0;
    }
    bool w_down(){
        return y1==::h;
    }
    bool w_left(){
        return x0==0;
    }
    bool w_right(){
        return x1==::w;
    }
    double ball_y(){
        if(w_up() && w_down())
            return (y0+y1)/2;
        if(w_up())return y0;
        if(w_down())return y1;
        return (y0+y1)/2;
    }
    double ball_x(){
        if(w_left() && w_right())
            return (x0+x1)/2;
        if(w_left())return x0;
        if(w_right())return x1;
        return (x0+x1)/2;
    }
    double area(){
        return w()*h();
    }
    btree* get_down(){
        if(down!=0)return down;
        down = new btree;
        if(w()>h()){
            down->x0=(x0+x1)/2;
            down->x1=x1;
            down->y0=y0;
            down->y1=y1;
        }else{
            down->x0=x0;
            down->x1=x1;
            down->y0=(y0+y1)/2;
            down->y1=y1;
        }
        //cout<<"created "<<area()<<" -> "<<down->area()<<"\n";
        return down;
    }
    btree* get_up(){
        if(up!=0)return up;
        up = new btree;
        if(w()>h()){
            up->x0=x0;
            up->x1=(x0+x1)/2;
            up->y0=y0;
            up->y1=y1;
        }else{
            up->x0=x0;
            up->x1=x1;
            up->y0=y0;
            up->y1=(y0+y1)/2;
        }
        //cout<<"created "<<area()<<" -> "<<up->area()<<"\n";
        return up;
    }
    bool is_split(){
        return down!=0 || up !=0;
    }
    bool add(int i){
        double rw,rh;
        int xm=1;
        int ym=1;
        if(w_left())xm++;
        if(w_right())xm++;
        if(w_up())ym++;
        if(w_down())ym++;

        rw = xm*w();
        rh = ym*h();
        if(xm==3)rw = 1e10;
        if(ym==3)rh = 1e10;
        //cout<<"rw = "<<rw<<" rh = "<<rh<<"\n";

        if(rw < ri[i]*2 || rh < ri[i]*2)
            return false;
        if(full)return false;
        if(rw > ri[i]*4 && rh > ri[i]*4){
            //split
            return 
            get_up()->add(i) ||
            get_down()->add(i);
        }else if(!is_split()){
            full = true;
            pos_x[i] = ball_x();
            pos_y[i] = ball_y();
            return true;
        }
        return false;
    }
};


int main(){
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        cin>>n>>w>>h;
        ri.resize(n);
        sr.resize(n);
        for(int i=0;i<n;i++){
            cin>>ri[i];
            sr[i].first=ri[i];
            sr[i].second=i;
        }

        std::sort(sr.rbegin(),sr.rend());
        btree b;
        b.x0=0;
        b.y0=0;
        b.x1=w;
        b.y1=h;
        for(size_t i=0;i<sr.size();i++){
            assert(b.add(sr[i].second));
        }
        cout<<"Case #"<<z<<": ";
        for(int i=0;i<n;i++){
            printf("%.7f %.7f ",pos_x[i],pos_y[i]);
        }
        cout<<"\n";
    }
}
