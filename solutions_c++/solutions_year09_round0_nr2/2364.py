#include<iostream>
#include<vector>

class Point
{
public:
Point(int a,int b):x(a),y(b)
{
}
int x,y;
};

int main()
{
    int numCases;
    std::cin>>numCases;
    for (int i=0;i<numCases;i++)
    {
        int x,y;
        std::cin>>x>>y;
        std::vector<std::vector<int> > matrix(x,std::vector<int >(y,0));
        for (int j=0;j<x;j++)
        {
            for (int k=0;k<y;k++)
            {
                std::cin>>matrix[j][k];
                //std::cout<<matrix[j][k];
            }
            //std::cout<<std::endl;
        }
        //std::cout<<std::endl;
        std::vector<std::vector<char> > fillBasin(x,std::vector<char >(y,'0'));
        char basin='a';
        std::vector<Point>  points;
        for (int J=0;J<x;J++)
        {
            for (int K=0;K<y;K++)
            {
               int sinkNotFound=true;
               int j=J,k=K;
               if (fillBasin[j][k]!='0')sinkNotFound=false;
               while(sinkNotFound)
               {
                  points.push_back(Point(j,k));
                  Point PN(j-1,k),PW(j,k-1),PE(j,k+1),PS(j+1,k),temp(-1,-1);
                  int max=1,sink=1;
                  if (PS.x<x)
                  {
                    if (matrix[PS.x][PS.y]>=matrix[j][k])
                    sink*=2;
                    else temp=PS;
                  }
                  else sink*=2;
                  if (PE.y<y)
                  {
                    if (matrix[PE.x][PE.y]>=matrix[j][k])
                    sink*=2;
                    else if (temp.x==-1)temp=PE;
                    else if (matrix[PE.x][PE.y]<=matrix[temp.x][temp.y])temp=PE;
                    
                  }
                  else sink*=2;
                  if (PW.y>=0)
                  {
                    if (matrix[PW.x][PW.y]>=matrix[j][k])
                    sink*=2;
                    else if (temp.x==-1)temp=PW;
                    else if (temp.x!=-1&&matrix[PW.x][PW.y]<=matrix[temp.x][temp.y])temp=PW;
                  }
                  else sink*=2;
                  if (PN.x>=0)
                  {
                    if (matrix[PN.x][PN.y]>=matrix[j][k])
                    sink*=2;
                    else if (temp.x==-1)temp=PN;
                    else if (temp.x!=-1&&matrix[PN.x][PN.y]<=matrix[temp.x][temp.y])temp=PN;
                  }
                  else sink*=2;
                  if (sink==16)
                  {
                      sinkNotFound=false; 
                      for(int l=0;l<points.size();l++)
                      {
                          fillBasin[points[l].x][points[l].y]=basin;
                          //std::cout<<"sink points "<<points[l].x<<" "<<points[l].y<<std::endl;
                      }
                      points.clear(); 
                      basin++;
                  }
                  else
                  {
                     if (fillBasin[temp.x][temp.y]!='0') 
                     {
                         char tempbasin=fillBasin[temp.x][temp.y];
                         for(int l=0;l<points.size();l++)
                         {
                             fillBasin[points[l].x][points[l].y]=tempbasin;
                             //std::cout<<"already filled points "<<points[l].x<<" "<<points[l].y<<std::endl;
                         }
                         points.clear();
                         sinkNotFound=false;
                     }
                     else
                     {
                         j=temp.x,k=temp.y;
                     }
                  }
               }
                
            }
        }
        std::cout<<"Case #"<<i+1<<":"<<std::endl;
        for(int u=0;u<x;u++)
        {
            for(int v=0;v<y;v++)
            {
                std::cout<<fillBasin[u][v]<<" ";
            }
            std::cout<<std::endl;
        }         

    }
    return 0;
}
