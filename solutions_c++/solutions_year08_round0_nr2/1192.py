#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>

using namespace std;

bool comp(vector<int> a, vector <int> b){ return (a[0]<b[0]);}

int main(int argc, char *argv[])
{
    ofstream fout ("a.out");
    ifstream fin ("a.in");
    vector < vector <int> > ab;
    vector < vector <int> > ba;
    int n;
    int t;
    int na;
    int nb;
    int resa;
    int resb;
    string temp;
    getline(fin, temp);
    stringstream ss;
    ss<<temp;
    ss>>n;
    
    for(int i=0; i<n; i++)
    {
        resa=0;
        resb=0;
        ab.clear();
        ba.clear();
        getline(fin, temp);
        stringstream sst;
        sst<<temp;
        sst>>t;
        getline(fin, temp);
        string tempa="";
        string tempb="";
        int which=0;
        for(int j=0; j<temp.length(); j++)
        {
            if(temp[j]==' ')
            {
                which=1;
            }
            else if(which==0)
            {
                tempa+=temp[j];
            }
            else if(which==1)
            {
                tempb+=temp[j];
            }
        }
        stringstream ssa;
        ssa<<tempa;
        ssa>>na;
        stringstream ssb;
        ssb<<tempb;
        ssb>>nb;
        
        for(int j=0; j<na; j++)
        {
            int h=0;
            int m=0;
            vector <int> train;
            string s;
            getline(fin, s);
            h=(((int)s[0]-48)*10+((int)s[1]-48));
            m=(((int)s[3]-48)*10+((int)s[4]-48));
            train.push_back(h*60+m);
            h=(((int)s[6]-48)*10+((int)s[7]-48));
            m=(((int)s[9]-48)*10+((int)s[10]-48));
            train.push_back(h*60+m);
            ab.push_back(train);
        }
        for(int j=0; j<nb; j++)
        {
            int h=0;
            int m=0;
            vector <int> train;
            string s;
            getline(fin, s);
            h=(((int)s[0]-48)*10+((int)s[1]-48));
            m=(((int)s[3]-48)*10+((int)s[4]-48));
            train.push_back(h*60+m);
            h=(((int)s[6]-48)*10+((int)s[7]-48));
            m=(((int)s[9]-48)*10+((int)s[10]-48));
            train.push_back(h*60+m);
            ba.push_back(train);
        }
        sort(ab.begin(), ab.end(), comp);
        sort(ba.begin(), ba.end(), comp);
        
        int k=0;
        int l=0;
        vector <int> aaa;
        vector <int> bbb;
        int traina=0;
        int trainb=0;
        while(k<(int)ab.size() || l<(int)ba.size())
        {
            if(k<(int)ab.size() && l<(int)ba.size() && ab[k][0]<ba[l][0])
            {
                if(!aaa.empty())
                {
                    for(int j=0; j<aaa.size(); j++)
                    {
                        if(aaa[j]<=ab[k][0])
                        {
                            aaa.erase(aaa.begin()+j);
                            traina++;
                            j--;
                            if(aaa.empty())
                            {
                                break;
                            }
                        }
                    }
                }
                
                if(traina>0)
                {
                    traina--;
                    bbb.push_back(ab[k][1]+t);
                }
                else
                {
                    resa++;
                    bbb.push_back(ab[k][1]+t);
                }
                k++;
            }
            else if(k<(int)ab.size() && l<(int)ba.size() && ab[k][0]>=ba[l][0])
            {
                if(!bbb.empty())
                {
                    for(int j=0; j<bbb.size(); j++)
                    {
                        if(bbb[j]<=ba[l][0])
                        {
                            bbb.erase(bbb.begin()+j);
                            trainb++;
                            j--;
                            if(bbb.empty())
                            {
                                break;
                            }
                        }
                    }
                }
                
                if(trainb>0)
                {
                    trainb--;
                    aaa.push_back(ba[l][1]+t);
                }
                else
                {
                    resb++;
                    aaa.push_back(ba[l][1]+t);
                }
                l++;
            }
            else if(k<(int)ab.size())
            {
                if(!aaa.empty())
                {
                    for(int j=0; j<aaa.size(); j++)
                    {
                        if(aaa[j]<=ab[k][0])
                        {
                            aaa.erase(aaa.begin()+j);
                            traina++;
                            j--;
                            if(aaa.empty())
                            {
                                break;
                            }
                        }
                    }
                }
                
                if(traina>0)
                {
                    traina--;
                    bbb.push_back(ab[k][1]+t);
                }
                else
                {
                    resa++;
                    bbb.push_back(ab[k][1]+t);
                }
                k++;
            }
            else if(l<(int)ba.size())
            {
                if(!bbb.empty())
                {
                    for(int j=0; j<bbb.size(); j++)
                    {
                        if(bbb[j]<=ba[l][0])
                        {
                            bbb.erase(bbb.begin()+j);
                            trainb++;
                            j--;
                            if(bbb.empty())
                            {
                                break;
                            }
                        }
                    }
                }
                
                if(trainb>0)
                {
                    trainb--;
                    aaa.push_back(ba[l][1]+t);
                }
                else
                {
                    resb++;
                    aaa.push_back(ba[l][1]+t);
                }
                l++;
            }
        }
        fout << "Case #" << (i+1) << ": " << resa << " " << resb << endl;
    }
    //system("PAUSE");
    return EXIT_SUCCESS;
}
