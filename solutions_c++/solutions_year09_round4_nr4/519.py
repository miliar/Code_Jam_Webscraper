#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

double dist(double x1,double y1,double x2,double y2)
{
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

double min(double x, double y)
{
    return (x<y)?x:y;
}
double max(double x, double y)
{
    return (x<y)?y:x;
}

double cir[50][3];

double cal3(int i, int j)
{
    //cout<<cir[3-i-j][2]<<endl;
    
    return max(cir[3-i-j][2], (dist(cir[i][0],cir[i][1],cir[j][0],cir[j][1]) + cir[i][2] + cir[j][2] )/2);
}

int main()
{
    // ifstream cin;
    // cin.open("C1.in");
    //cin.open("B-small-attempt0.in");
    //cin.open("B-large.in");
    //ofstream cout;
    //cout.open(
    
    int n;
    cin>>n;

    for (int i=0; i<n; ++i){
        int k;
        cin>>k;
        
        for (int j = 0; j<k;++j)
        {
            cin>> cir[j][0] >> cir[j][1] >> cir[j][2];
            //cout<< cir[j][0] << cir[j][1] << cir[j][2];
        }
        
        double ans = 0;

        if (k == 1)
            ans = cir[0][2];
        else if (k==2)
            ans = max(cir[0][2], cir[1][2]);
        else if (k==3)
            ans = min( cal3(0,1), min(cal3(0,2), cal3(1,2)));

        // cout<< cal3(0,1)<<endl;
        // cout<< cal3(0,2)<<endl;
        // cout<< cal3(2,1)<<endl;
        //getline(cin,str);
        cout<<"Case #"<<i+1<<": "<< ans <<endl;
    }
    
    //cin.close();
    
}
