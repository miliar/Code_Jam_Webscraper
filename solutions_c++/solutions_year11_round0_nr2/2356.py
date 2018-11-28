#include <iostream>
#include <stack>
#include <map>
#include <string>

using namespace std;

char arr[100]; 

int TC = 1, T, N, C, D, Pos, Index, new_pos, found=0;;
string S,s,temp1,temp2;
char c0,c1,Prev,Cur;

multimap<char,char> allpair;
multimap<char,char>::iterator it1;
pair<multimap<char,char>::iterator,multimap<char,char>::iterator> ret;

map<string,char> pairs;
map<string,char>::iterator it2;

multimap<char,char> opp;
multimap<char,char>::iterator it3;

multimap<char,int> del;
multimap<char,int>::iterator it4,tmp4;
pair<multimap<char,int>::iterator,multimap<char,int>::iterator> ret2;

void new_variables()
{
    del.clear();
    allpair.clear();
    pairs.clear();
    opp.clear();
}


void del_check()
{
    char x;
    for (it4=del.begin();  it4!=del.end(); )
    {
        if((*it4).second>=Pos)
        {
            tmp4=it4;
            it4++;
            del.erase(tmp4);
        }
        else
            it4++;
    }
    /*cout<<"del contains: "<<endl;
    for (it4=del.begin();  it4!=del.end(); it4++)
    {
        cout<<(*it4).first<<"->"<<(*it4).second<<endl;
    }*/
}

void Check()
{
    //cout<<"Pos="<<Pos<<endl;
    if(Pos==0)
    {
        Prev=Cur;
        arr[Pos]=Cur;
        if(opp.count(Cur)>0)
            del.insert(pair<char,int>(Prev,Pos));
        Pos++;
        //cout<<"prev= NULL and cur= "<<Cur<<endl;
        return;
    }
    //cout<<"prev= "<<Prev<<" and cur= "<<Cur<<endl;
    if(allpair.count(Cur)>0)
    {
        //cout<<Cur<<" in allpairs"<<endl;
        if(allpair.count(Prev)>0)
        {
            //cout<<Prev<<" also in allpairs"<<endl;
            temp1="";
            temp2="";
            temp1.insert(0,1,Cur);
            temp1.insert(1,1,Prev);
            
            temp2.insert(0,1,Prev);
            temp2.insert(1,1,Cur);
            
            //cout<<"temp1= "<<temp1<<" and temp2= "<<temp2<<endl;
            
            if(pairs.count(temp1)>0)
            {
                //cout<<"Substitute "<<temp1<<" for "<<pairs[temp1]<<endl;
                Pos--;
                arr[Pos]=pairs[temp1];
                Prev=arr[Pos];
                del_check();
                Pos++;
                return;
            }
            else if(pairs.count(temp2)>0)
            {
                //cout<<"Substitute "<<temp2<<" for "<<pairs[temp2]<<endl;
                Pos--;
                arr[Pos]=pairs[temp2];
                Prev=arr[Pos];
                del_check();
                Pos++;
                return;
            }
        }
    }
    arr[Pos]=Cur;
    Prev=arr[Pos];
    Pos++;
    if(opp.count(Cur)>0)
    {
        //cout<<Cur<<" in opp"<<endl;
        new_pos=-1;
        ret=opp.equal_range(Cur);
        for (it3=ret.first; it3!=ret.second; ++it3)
        {
            if(del.count((*it3).second)>0)
            {
                //cout<<"found "<<(*it3).first<<" at "<<Pos<<" and "<<(*it3).second<<" at "<<del[(*it3).second]<<"\n";
                found=1;
            }
        }
        if(found)
        {
            Pos=0;
            del_check();
            found=0;
        }
        else
        {
            del.insert(pair<char,int>(Prev,Pos-1));
        }
    }
}

void print_()
{
    int i;
    cout<<"[";
    for (i =0; i<Pos-1; i++)
    {
        cout<<arr[i]<<", ";
    }
    if(Pos>0)
    cout<<arr[i];
    cout<<"]\n";
}

int main ()
{
    cin>>T;
    for (; TC <= T; TC++)
    {
        new_variables();
        cin>>C;
        while(C--)
        {
            cin>>S;
            pairs[S.substr(0,2)]=S.at(2);
            c0=S.at(0);
            c1=S.at(1);
            allpair.insert(pair<char,int>(c0,c1));
            allpair.insert(pair<char,int>(c1,c0));
        }
        /*
        for ( it=allpair.begin() ; it != allpair.end(); it++ )
                cout << (*it).first << " => " << (*it).second << endl;
        */
        
        cin>>D;
        while(D--)
        {
            cin>>S;
            c0=S.at(0);
            c1=S.at(1);
            opp.insert(pair<char,int>(c0,c1));
            opp.insert(pair<char,int>(c1,c0));
        }
        cin>>N;
        cin>>S;
        Pos=0;
        Index=0;
        Cur=S[Index];
        Check();
        Index++;
        for (int i =1; i<N;i++)
        {
            Cur=S[Index];
            Check();
            Index++;
            
        }
        printf ("Case #%d: ", TC);
        print_();
    }

    return 0;
}
