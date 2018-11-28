#include <iostream>
#include <vector>
#include <string>
using namespace std;



__inline__ int getdirection(int y, int x, vector<vector<int> > m) {
  int mmin=100000;

  for(int i=-1; i<=1; i++) {
    for(int j=-1; j<=1; j++) {
      if((i==0 || j==0) && i!=j) {
        if(m[y+i][x+j]<mmin) mmin=m[y+i][x+j];
      }
    }
  }


  if(m[y-1][x]==mmin) return 0;
  if(m[y][x-1]==mmin) return 1;
  if(m[y][x+1]==mmin) return 2;
  if(m[y+1][x]==mmin) return 3;


  //direction:  0 N,  1 W,  2 E,  3 S

}



void floodfill(int x, int y, int id, vector<vector<int> > m, vector<vector<int> > &fill, int w, int h) {
  fill[y-1][x-1]=id;

  for(int i=-1; i<=1; i++) {
    for(int j=-1; j<=1; j++) {
      if((i==0 || j==0) && i!=j && (y+i>=1 && y+i<h+1 && x+j>=1 && x+j<w+1) && m[y+i][x+j]>m[y][x]) {
        //will y+i, x+j  flow into x, y?

        int dir=getdirection(y+i, x+j, m);
//cout<<dir<<" "<<i<<" "<<j<<endl;
        if((dir==0 && i==1) || (dir==1 && j==1) || (dir==2 && j==-1) || (dir==3 && i==-1)) floodfill(x+j, y+i, id, m, fill, w, h);

      }
    }
  }

}





int main() {
  int t;
  scanf("%d", &t);
  for(int iii=1; iii<=t; iii++) {
    int h, w;
    scanf("%d %d", &h, &w);

    vector<vector<int> > m;
    vector<int> tmp(w+2, 100000);
    m.push_back(tmp);

    for(int y=0; y<h; y++) {
      vector<int> xx(w+2, 100000);
      for(int x=0; x<w; x++) {
        int t;
        scanf("%d", &t);
        xx[x+1]=t;
      }
      m.push_back(xx);
    }
    m.push_back(tmp);


/*
    for(int y=0; y<h+2; y++) {
      for(int x=0; x<w+2; x++) {
        cout<<m[y][x]<<" ";
      }
      cout<<endl;
    }
*/



    vector<vector<int> > fill;
    for(int i=0; i<h; i++) {
      vector<int> tt(w, 0);
      fill.push_back(tt);
    }


    int id=-1;
    for(int y=0; y<h; y++) {
      for(int x=0; x<w; x++) {
        int X=x+1;
        int Y=y+1;

        //is sink?
        int sink=1;

        for(int i=-1; i<=1; i++) for(int j=-1; j<=1; j++) {
          if(m[Y+i][X+j]<m[Y][X]  && (i==0 || j==0) && i!=j) sink=0;
        }


        if(sink==1) {
          floodfill(X, Y, id, m, fill, w, h);
          id--;
        }

      }
    }


/*
    for(int y=0; y<h; y++) {
      for(int x=0; x<w; x++) {
        cout<<fill[y][x]<<" ";
      }
      cout<<endl;
    }
*/



   char c='a';
   for(int y=0; y<h; y++) {
     for(int x=0; x<w; x++) {
       if(fill[y][x]<0) {
         int r=fill[y][x];
         for(int i=0; i<fill.size(); i++) for(int j=0; j<fill[0].size(); j++) if(fill[i][j]==r) fill[i][j]=c;

         c++;
       }

     }
   }




   cout<<"Case #"<<iii<<":"<<endl;
   for(int y=0; y<h; y++) {
     for(int x=0; x<w-1; x++) cout<<(char)(fill[y][x])<<" ";
     cout<<(char)(fill[y][w-1])<<endl;
   }

/*
    for(int y=0; y<h; y++) {
      for(int x=0; x<w; x++) {
        cout<<fill[y][x]<<" ";
      }
      cout<<endl;
    }


return 0;*/




  }

  return 0;
}

