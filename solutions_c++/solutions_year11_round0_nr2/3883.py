/*
 *  Author: BK691
 */

#include <iostream>
#include <vector>

using namespace std;

string RunTestCase(const string &invoking, vector< char > &element_list, const vector< string > &combo, const vector< string > &opposed);
void InvokeBaseElement(vector< char > &element_list, const char &element, const vector< string > &combo, const vector< string > &opposed);
void Combine(vector< char > &element_list, const vector< string > &combo);
void Oppose(vector< char > &element_list, const vector< string > &opposed);

int main()
{
    int T = 0;
    int C = 0;
    int D = 0;
    int N = 0;
    int test_index = 0;
    int c_index = 0;
    int d_index = 0;
    string c_str;
    string d_str;

    cin >> T;

    vector< char >* element_list = new vector< char >[ T ];
    vector< string >* combo = new vector< string >[ T ];
    vector< string >* opposed = new vector< string >[ T ];
    string* invoking = new string[ T ];

    while(test_index < T)
    {
        c_index = 0;
        d_index = 0;

        cin >> C;
        
        while(c_index < C)
        {
            cin >> c_str;

            combo[ test_index ].push_back( c_str );

            ++c_index;
        }

        cin >> D;

        while(d_index < D)
        {
            cin >> d_str;

            opposed[ test_index ].push_back( d_str );

            ++d_index;
        }

        cin >> N;

        cin >> invoking[ test_index ];

        ++test_index;
    }

    for(int i = 0; i < T; ++i)
        cout << "Case #" << (i + 1) << ": " << RunTestCase( invoking[ i ], element_list[ i ], combo[ i ], opposed[ i ] ) << endl;

    // Deallocation of dynamic memory

    delete[] element_list;
    delete[] combo;
    delete[] opposed;
    delete[] invoking;

    element_list = NULL;
    combo = NULL;
    opposed = NULL;
    invoking = NULL;

    return 0;
}

string RunTestCase(const string &invoking, vector< char > &element_list, const vector< string > &combo, const vector< string > &opposed)
{
    string display = "[";

    for(unsigned int i = 0; i < invoking.size(); ++i)
        InvokeBaseElement( element_list, invoking[ i ], combo, opposed );

    for(unsigned int i = 0; i < element_list.size(); ++i)
    {
        display += element_list[ i ];

        if(i < (element_list.size() - 1))
            display += ", ";
    }

    display += "]";

    return display;
}

void InvokeBaseElement(vector< char > &element_list, const char &element, const vector< string > &combo, const vector< string > &opposed)
{
    element_list.push_back( element );

    if(element_list.size() > 1)
    {
        Combine(element_list, combo);
        Oppose(element_list, opposed);
    }
}

void Combine(vector< char > &element_list, const vector< string > &combo)
{
    for(unsigned int index = 0; index < combo.size(); ++index)
    {
        if( (element_list[ (element_list.size() - 1) ] == combo[ index ][ 0 ] && 
            element_list[ (element_list.size() - 2) ] == combo[ index ][ 1 ] ) ||
            (element_list[ (element_list.size() - 1) ] == combo[ index ][ 1 ] && 
            element_list[ (element_list.size() - 2) ] == combo[ index ][ 0 ] ) )
        {
            element_list.resize( (element_list.size() - 1) );
            element_list[ (element_list.size() - 1) ] = combo[ index ][ 2 ]; 
        }
    }
}

void Oppose(vector< char > &element_list, const vector< string > &opposed)
{
    bool found_element_1 = false;
    bool found_element_2 = false;

    for(unsigned int index = 0; index < opposed.size(); ++index)
    {
        for(unsigned int i = 0; i < element_list.size(); ++i)
        {
            if(!found_element_1)
                found_element_1 = opposed[ index ][ 0 ] == element_list[ i ];

            if(!found_element_2)
                found_element_2 = opposed[ index ][ 1 ] == element_list[ i ];

            if(found_element_1 && found_element_2)
                break;
        }


        if(found_element_1 && found_element_2)
            break;
    }


    if(found_element_1 && found_element_2)
        element_list.clear();

}


