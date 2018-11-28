#include<algorithm>
#include<iostream>
#include<set>
#include<map>
#include<string>
#include<vector>

using namespace std;

map<char, vector<int> > m;
vector<string> words;
int l, d, n;

void createMap()
{
    sort( words.begin(), words.end() );
    int start, end;
    char c = words[0][0];
    start = 0;
    for( int i = 0; i < words.size(); i++ )
    {
        if( c != words[i][0] )
        {
            vector<int> temp;
            temp.push_back( start );
            temp.push_back( i );
            m[c] = temp;
            c = words[i][0];
            start = i;
        }
    }
    vector<int> temp;
    temp.push_back( start );
    temp.push_back( words.size() );
    m[c] = temp;
}


void takeInput( int n )
{
    string temp;
    for( int i = 0; i < n; i++ )
    {
        cin>>temp;
        //cout<<temp<<endl;
        words.push_back( temp );
    }

}

void displayWords()
{
    cout<<"\tDisplaying words :"<<endl;
    for( int i = 0; i < words.size(); i++ )
        cout<<words[i]<<endl;
}

void displayMap()
{
    vector<int> temp;
    for( map<char, vector<int> >::iterator i = m.begin(); i != m.end(); i++ )
    {
        temp = (*i).second;
        cout<<(*i).first;
        cout<<" ";
        for( int j = 0; j < 2; j++ )
            cout<<temp[j]<<" ";
        cout<<endl;
    }
}

long long solve()
{
    string input;
    vector<char> firstLetter;
    cin>>input;
    vector< set<char> > s;
    int pos = 0;
    for( int i = 0; i < l; i++ )
    {
        set<char> tempSet;
        if( i == 0 )
        {
            if( input[0] == '(' )
            {
                pos = 1;
                while( input[pos] != ')' )
                    firstLetter.push_back( input[pos++] );
                pos++;
            }
            else
                firstLetter.push_back( input[pos++] );
            tempSet.clear();
            s.push_back(tempSet);
        }
        else
        {
            if( input[pos] == '(' )
            {
                pos++;
                while( input[pos] != ')' )
                    tempSet.insert( input[pos++] );
                pos++;
                s.push_back(tempSet);
            }
            else
            {
                tempSet.insert( input[pos++] );
                s.push_back(tempSet);
            }
        }
    }

    long long result = 0;

    for( int i = 0; i < firstLetter.size(); i++ )
    {
        map<char, vector<int> >::iterator iter = m.find( firstLetter[i] );
        if( iter != m.end() )
        {
            int start, end;
            vector<int> temp;
            temp = (*iter).second;
            start = temp[0];
            end = temp[1];
            for( int j = start; j < end; j++ )
            {
                int k;
                for( k = 1; k < l; k++ )
                {
                    set<char>::iterator setIter = s[k].find( words[j][k] );
                    if( setIter == s[k].end() )
                        break;
                }
                if( k == l )
                    result++;
            }
        }
    }
    return result;
}

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen( "largeOut.out", "w", stdout );

    cin>>l>>d>>n;
    takeInput(d);
    createMap();
    //displayWords();
    //displayMap();

    for( int i = 0; i < n; i++ )
    {
        cout<<"Case #"<<i+1<<": "<<solve()<<endl;
    }

}
