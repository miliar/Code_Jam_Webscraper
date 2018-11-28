#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int abs(int a)
{
    if(a>=0)
    return a;
    else
    return -a;
}

bool isCheck(vector<int> a , vector<int> b, vector<int> c, int s)
{
    int i,j,count=0;
    vector<bool> flag(3,false);

    for(i=0;i<3;i++)
    {
        for(j=(i+1);j<3;j++)
        {
            if(abs(a[i]-a[j])>=2 && !flag[0])
            {
                count++;
                flag[0]=true;
            }
            if(abs(b[i]-b[j])>=2 && !flag[1])
            {
                count++;
                flag[1]=true;
            }if(abs(c[i]-c[j])>=2 && !flag[2])
            {
                count++;
                flag[2]=true;
            }
        }
    }
    if(count == s)
     return true;
    else
     return false;
}

bool isCheck(vector<int> a , vector<int> b, int s)
{
    int i,j,count=0;
    vector<bool> flag(2,false);

    for(i=0;i<3;i++)
    {
        for(j=(i+1);j<3;j++)
        {
            if(abs(a[i]-a[j])>=2 && !flag[0])
            {
                count++;
                flag[0]=true;
            }
            if(abs(b[i]-b[j])>=2 && !flag[1])
            {
                count++;
                flag[1]=true;
            }
        }
    }
    if(count == s)
     return true;
    else
     return false;
}

bool isCheck(vector<int> a, int s)
{
    int i,j,count=0;
    vector<bool> flag(1,false);

    for(i=0;i<3;i++)
    {
        for(j=(i+1);j<3;j++)
        {
            if(abs(a[i]-a[j])>=2 && !flag[0])
            {
                count++;
                flag[0]=true;
            }

        }
    }
    if(count == s)
     return true;
    else
     return false;
}

int  calculate(vector<int> a , vector<int> b, vector<int> c, int p)
{
    int i,j,count=0;
    vector<bool> flag(3,false);

    for(i=0;i<3;i++)
    {
        if(a[i]>=p && !flag[0])
        {
            count++;
            flag[0]=true;
        }
        if(b[i]>=p && !flag[1])
        {
            count++;
            flag[1]=true;
        }
        if(c[i]>=p && !flag[2])
        {
            count++;
            flag[2]=true;
        }
    }
    return count;
}

int  calculate(vector<int> a , vector<int> b, int p)
{
    int i,j,count=0;
    vector<bool> flag(2,false);

    for(i=0;i<3;i++)
    {
        if(a[i]>=p && !flag[0])
        {
            count++;
            flag[0]=true;
        }
        if(b[i]>=p && !flag[1])
        {
            count++;
            flag[1]=true;
        }
    }
    return count;
}

int  calculate(vector<int> a , int p)
{
    int i,j,count=0;
    vector<bool> flag(1,false);

    for(i=0;i<3;i++)
    {
        if(a[i]>=p && !flag[0])
        {
            count++;
            flag[0]=true;
        }
    }
    return count;
}


void allPossibleScores(int score,vector<vector<vector<int> > >& all,int n)
{
    int k;
    for(int i=0;i<=10;i++)
    {
            for(int j=0;j<=10;j++)
            {
                k = score - i - j;
                if((k>=0) && (k<=10)  && (abs(i-j)<=2) && (abs(i-k)<=2) && (abs(k-j)<=2) )
                {
                    vector<int> temp;
                    temp.push_back(i);
                    temp.push_back(j);
                    temp.push_back((score)-(i+j));
                  //  cout<<"here";
                   // vector<vector<int> > temp1;
                   // temp1.push_back(temp);
                    all[n].push_back(temp);
                }
            }

    }
}

main()
{
    ifstream ifs;
    ifs.open("input.txt");
    ofstream ofs;
    ofs.open("output.txt");
    int t,z;
    ifs>>t;
    for(z=0;z<t;z++)
    {
    int n,s,i,j,k,p;
    ifs>>n>>s>>p;
    vector<vector<vector<int> > > all;
    all.resize(n);
    for(i=0;i<n;i++)
    {
        int l;
        ifs>>l;
        allPossibleScores(l,all,i);
    }
  //  for(i=0;i<all.size();i++)
    //{
      //  for(j=0;j<all[i].size();j++)
        //{
            //cout<<all[i].size();
          //  for(k=0;k<all[i][j].size();k++)
            //{
                //cout<<all[i][j][k]<<" ";
            //}
            //cout<<endl;
        //}
        //cout<<endl;
    //}
    int no;
    int max=0;
   // cout<<all[0].size()<<endl;
    for(i=0;i<all[0].size();i++)
    {
        if(n>1)
        {
            for(j=0;j<all[1].size();j++)
            {
                if (n>2)
                {
                    for(k=0;k<all[2].size();k++)
                    {
                        if(isCheck(all[0][i],all[1][j],all[2][k],s))
                        {
                          no=calculate(all[0][i],all[1][j],all[2][k],p);
                          if(no>max)
                          {
                              max=no;
                          }
                        }
                    }
                }
                else
                {
                    if(isCheck(all[0][i],all[1][j],s))
                        {
                          no=calculate(all[0][i],all[1][j],p);
                          if(no>max)
                          {
                              max=no;
                          }
                        }
                }
            }
        }
        else
        {
           // cout<<isCheck(all[0][i],s)<<endl;
            if(isCheck(all[0][i],s))
                        {
                          no=calculate(all[0][i],p);
                          if(no>max)
                          {
                              max=no;
                          }
                        }
        }
    }
 ofs<<"Case #"<<(z+1)<<": "<<max<<endl;
    }
    ifs.close();
    ofs.close();
}
