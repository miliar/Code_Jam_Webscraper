#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<cstdio>
using namespace std;

bool is_combine( string cb, char first, char second )
{
    if( cb[0]==first && cb[1]==second )
        return true;
    if( cb[1]==first && cb[0]==second )
        return true;

    return false;
}

char check_combine(vector<string> & cb_list, char c1, char c2 ) {

    for(int i=0;i<cb_list.size();++i) {
        if( is_combine(cb_list[i], c1, c2) ) {
            return cb_list[i][2];
        }
    }

    return NULL;
}

bool check_opposed( vector<string> & op_list, char c1, char c2) {

    for(int i=0;i<op_list.size();++i) {
        if( op_list[i][0]==c1 && op_list[i][1]==c2)
            return true;
        if( op_list[i][1]==c1 && op_list[i][0]==c2)
            return true;
    }
    return false;
}

string do_magicka( string & line )
{

    istringstream sin(line);
    //cout<<"line: "<<line<<endl;

    // read combine sets
    int len_combine;
    sin>>len_combine;

    vector<string> combine_list;

    for(int i=0; i<len_combine; ++i) {
        string combine;
        sin>>combine;
        combine_list.push_back(combine);
    }

    // read oppoosed sets
    int len_opposed;
    sin>>len_opposed;

    vector<string> opposed_list;

    for(int i=0; i<len_opposed; ++i) {
        string opposed;
        sin>>opposed;
        opposed_list.push_back(opposed);
    }

    // process works
    int len_input;
    sin>>len_input;

    sin.ignore(100, ' ');

    vector<char> my_list;

    char elem;

    sin>>elem;
    my_list.push_back(elem);

    while( sin >> elem ) {

        // check combine
        while ( 1 ) {

            char result = check_combine(combine_list, elem, my_list.back() );

            if( result == 0) break;

            elem = result;
            my_list.pop_back();
        }
        my_list.push_back(elem);

        // check opposed
        for(int i=0;i<my_list.size()-1;++i) {
            if ( check_opposed(opposed_list,  my_list[i], my_list.back() ) ) {
                my_list.clear();
                break;
            }
        }

    }
    ostringstream sout;
    sout<<'[';
    for(int i=0;i<my_list.size();++i)  {
        sout<<my_list[i];

        if( i!=my_list.size()-1 )
            sout<<", ";
    }
    sout<<']';
    return sout.str();
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int num_case;
    scanf("%d ", &num_case);

    for(int i=1; i<=num_case; ++i) {

        string line;
        getline(cin, line);

        string output = do_magicka(line);

        printf("Case #%d: %s\n", i , output.c_str());
    }
    return 0;
}
