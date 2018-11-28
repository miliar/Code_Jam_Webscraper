# include <iostream>
# include <vector> 
# include <queue>
using namespace std;

int main ()
{
    int test,test1=1;;
    cin>>test;
    while (test--)
    {
          int array [101][101];
          char array1 [101][101];
          vector < vector <int> > arr;
          int row,col;
          cin>>row>>col;
          for (int i=0;i<row;i++)
          {
              for (int j=0;j<col;j++)
              {
                  cin>>array[i][j];
              }
          }
          for (int i=0;i<row;i++)
          {
              for (int j=0;j<col;j++)
              {
                  int val=array[i][j];
                  array1[i][j]='A';
                  if ((i-1)>=0&&(array[i-1][j]<val))
                  {
                        val=array[i-1][j];
                        array1[i][j]='N';
                  }
                  if ((j-1)>=0&&(array[i][j-1]<val))
                  {
                        val=array[i][j-1];
                        array1[i][j]='W';
                  }
                  if ((j+1)<col&&(array[i][j+1]<val))
                  {
                        val=array[i][j+1];
                        array1[i][j]='E';
                  }
                  if ((i+1)<row&&(array[i+1][j]<val))
                  {
                        val=array[i+1][j];
                        array1[i][j]='S';
                  }
                  //cout<<array1[i][j]<<" ";
                  if (array1[i][j]=='A')
                  {
                        vector <int> sss;
                        sss.push_back (i);
                        sss.push_back (j);
                        arr.push_back (sss);
                  }      
              }
              //cout<<endl;
          }
          bool array2[101][101];
          memset (&array2,false,sizeof(array2));
          int array3[101][101];
          char a='a';
          for (int i=0;i<arr.size ();i++)
          {
              vector <int> q=arr[i];
              int k,l;
              k=q[0];
              l=q[1];
              array3[k][l]=i+1;
              queue <vector <int> > ggg;
              ggg.push(q);
              while (ggg.size ()!=0)
              {
                    vector <int> jjj=ggg.front();
                    k=jjj[0];
                    l=jjj[1];
                    if ((k+1)<row&&(array1[k+1][l]=='N'))
                    {
                          array3[k+1][l]=i+1;
                          vector <int> sss;
                          sss.push_back (k+1);
                          sss.push_back (l);
                          ggg.push (sss);
                    }
                    if ((k-1)>=0&&(array1[k-1][l]=='S'))
                    {
                          array3[k-1][l]=i+1;
                          vector <int> sss;
                          sss.push_back (k-1);
                          sss.push_back (l);
                          ggg.push (sss);
                    }                                       
                    if ((l+1)<col&&(array1[k][l+1]=='W'))
                    {
                          array3[k][l+1]=i+1;
                          vector <int> sss;
                          sss.push_back (k);
                          sss.push_back (l+1);
                          ggg.push (sss);
                    }                       
                    if ((l-1)>=0&&(array1[k][l-1]=='E'))
                    {
                          array3[k][l-1]=i+1;
                          vector <int> sss;
                          sss.push_back (k);
                          sss.push_back (l-1);
                          ggg.push(sss);
                    }
                    ggg.pop();
              }
          }
          bool array4[27];
          memset (array4,false,sizeof (array4));
          char array5[27];
          char array6[101][101]; 
          for (int i=0;i<row;i++)
          {
              for (int j=0;j<col;j++)
              {
                    if (array4[array3[i][j]]==false)
                    {
                           array4[array3[i][j]]=true;
                           array5[array3[i][j]]=a;
                           a++;
                    }
                    array6[i][j]=array5[array3[i][j]];
              }
          }   
          cout<<"Case #"<<test1<<":"<<endl;                                            
          for (int i=0;i<row;i++)
          {
              for (int j=0;j<col;j++)
              {
                  cout<<array6[i][j]<<" ";
              }
              cout<<endl;
          }                                
          test1++;                              
    }
    return 0;
}                                                                    
