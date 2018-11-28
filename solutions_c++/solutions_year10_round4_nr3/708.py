# include <iostream>

using namespace std;

int array1[202][202];
int array2[202][202];

int main ()
{
    int test,count=1;
    cin>>test;
    while (count<=test)
    {
          int rect,x1,x2,y1,y2;
          int maxy,maxx,minx,miny;
          minx = miny = 101;
          maxx = maxy = 0;
          cin>>rect;
          memset (array1,0,sizeof(array1)); 
          for (int x=0;x<rect;x++)
          {
           cin>>x1>>y1>>x2>>y2;
           minx = std::min (minx,x1); 
           miny = std::min (miny,y1);
           maxx = std::max (maxx,x2);
           maxy = std::max (maxy,y2);  
           for (int i=x1;i<=(x2);i++)
           {
               for (int j=y1;j<=(y2);j++)
                 {
                   array1[i][j] = 1;
                  }
           }
          }
          long long ans = 0;
          bool flag = true;
          while (flag)
          {
              flag = false;  
              memset (array2,0,sizeof(array2));
              for (int i=1;i<201;i++)
              {
                  for (int j=1;j<201;j++)
                  {
                      if (array1[i][j] == 1)
                      {
                          if (array1[i-1][j] == 0 && array1[i][j-1] == 0)
                          {
                              array2[i][j] = 0;
                          }
                          else
                          {
                              array2[i][j] = 1;
                              flag = true;
                          }    
                      }
                      if (array1[i][j] == 0)
                      {
                          if (array1[i-1][j] ==1 && array1[i][j-1] == 1)
                          {
                              array2[i][j] = 1;
                              flag = true;
                          }
                          else
                          {
                              array2[i][j] = 0;
                          }
                      }
                  }
              }
              memcpy (array1,array2,sizeof(array1));
              ans++;
          }                                                                                 
          cout<<"Case #"<<count<<": "<<ans<<endl; 
          count++;
    }
    return 0;
}         
