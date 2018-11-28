#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<conio.h>
using namespace std;
    
int x, y;
int** map;
char** marked_map;
int character = 97;
bool checko = 0;
int val(int i, int j)
{
    if (i >= 0 && i < y && j >=0 && j < x)
    {
       return map[i][j];      
    }
    return 100000;
}

char findmin(int n, int w, int e, int s)
{
     int min = 100000;
     char ret;
     if (s <= min) {min = s; ret = 's';}
     if (e <= min) {min = e; ret = 'e';}
     if (w <= min) {min = w; ret = 'w';}
     if (n <= min) {min = n; ret = 'n';}
     
     return ret;
}

bool find(vector<int> tox, vector<int> toy,int k, int j)
{
      for (int i = 0; i < tox.size(); i++)
      {
          if (tox[i]==j)
          {
             if (toy[i]==k) return true;              
          }    
      }
      return false;
}

void evaluate(int i , int j, vector<int> to_mark_x, vector<int> to_mark_y)
{
     if (marked_map[i][j] != '#')
     {
         for (int q = 0; q < to_mark_x.size(); q++)
         {
             marked_map[to_mark_y[q]][to_mark_x[q]] = marked_map[i][j];    
         } 

        return;                     
     }

     char dir = findmin(val(i-1,j), val(i,j-1), val(i,j+1), val(i+1,j));
     //fwriter << i << " " << j << " " << dir << endl;
     to_mark_x.push_back(j);
     to_mark_y.push_back(i);

     if (dir == 'n' && (val(i-1,j) < val(i,j)))
     {
     if(find(to_mark_x,to_mark_y,i-1,j)) return;
     evaluate(i-1,j,to_mark_x,to_mark_y);
     }
     else if (dir == 'w' && (val(i,j-1) < val(i,j)))
     {
     if(find(to_mark_x,to_mark_y,i,j-1)) return;
     evaluate(i,j-1,to_mark_x,to_mark_y);
     }
     else if (dir == 'e' && (val(i,j+1) < val(i,j)))
     {
     if(find(to_mark_x,to_mark_y,i,j+1)) return;
     evaluate(i,j+1,to_mark_x,to_mark_y);
     }
     else if (dir == 's' && (val(i+1,j) < val(i,j)))
     {
     if(find(to_mark_x,to_mark_y,i+1,j)) return;
     evaluate(i+1,j,to_mark_x,to_mark_y);
     }
     else
     {
          for (int i = 0; i < to_mark_x.size(); i++)
         {
             marked_map[to_mark_y[i]][to_mark_x[i]] = character;    
         }   
         character++; 
     }
}

int main()
{
    ifstream freader("B-small.in");
    ofstream fwriter("B-small.out");
    int N;
    freader >> N;
    //cout << N;
    for (int i = 0; i < N; i++)
    {
        character = 97;
        freader >> y >> x;
        
        map = new int*[y];
        marked_map = new char*[y];
        for (int i = 0; i < y; i++)
        {
            map[i] = new int[x];    
            marked_map[i] = new char[x];
        }
        
        for (int i = 0; i < y; i++)
        {
            for (int j = 0; j < x; j++)
            {
                marked_map[i][j] = '#';
                freader >> map[i][j];
                //cout << map[i][j] << " ";
            }
            //cout << endl;    
        }
        //cout << endl;
        
        //--------------------
        
        for(int i = 0; i < y; i++)
        {
                for (int j = 0; j < x; j++)
                {
                    vector<int> tox, toy;
                    evaluate(i,j,tox,toy);
                }        
        }
        fwriter << "Case #" << i+1 << ":" << endl;
//        for (int i = 0; i < y; i++)
//        {
//            for (int j = 0; j < x; j++)
//            {
//                
//                fwriter << map[i][j];
//                if (j != x-1) fwriter  << " ";
//            }
//            fwriter << endl;
//        }
//        fwriter << endl;
        for (int i = 0; i < y; i++)
        {
            for (int j = 0; j < x; j++)
            {
                
                fwriter << marked_map[i][j];
                if (j != x-1) fwriter  << " ";
            }
            fwriter << endl;
        }
        //getch();
        //system("PAUSE");
        //--------------------
        
        
        for (int i = 0; i < y; i++)
        {
            delete map[i];
            delete marked_map[i];
        }
        delete map;
        delete marked_map;
    }
    
    //system("PAUSE");
    fwriter.close();
    freader.close();
    return 0;   
}
