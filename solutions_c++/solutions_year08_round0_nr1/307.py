#include <vector>
#include <stack>
#include <map>
#include <iostream>
#include <fstream>
#include <strstream>
#include <string>
#include <algorithm>

using namespace std;

int Solve(vector<string> servers, vector<string> requests)
{
    if(requests.size() == 0)
        return 0;

    vector<vector<int> > data;
    data.resize(requests.size(), vector<int>() );
    for(size_t i = 0; i<data.size(); ++i) {
        data[i].resize(servers.size(), 0);
    }

    //////////////////////////////////////////////////////////////
    /*cout<<data.size()<<'x'<<data[0].size()<<endl;
    for(size_t i = 0; i<servers.size(); i++)
        cout<<servers[i]<<", ";
    cout<<endl;
    for(size_t i = 0; i<requests.size(); i++)
        cout<<requests[i]<<", ";
    cout<<endl;
    // */ ///////////////////////////////////////////////////////


    // First line:
    string req = requests[requests.size() - 1];

    for(size_t srv = 0; srv<servers.size(); ++srv) {
        if(servers[srv] != req)
            data[0][srv] = 0;
        else
            data[0][srv] = 1;
    }

    for(size_t req_len = 1; req_len<requests.size(); ++req_len) {

        string req = requests[requests.size() - req_len - 1];

        for(size_t srv = 0; srv<servers.size(); ++srv) {
            if(servers[srv] != req)
                data[req_len][srv] = data[req_len-1][srv];
            else {
                // Find minimum server to switch
                int min_val = 100000000;
                for(size_t j = 0; j<servers.size(); ++j) {
                    if(servers[j] == req) 
                        continue;
                    if(data[req_len-1][j] < min_val)
                        min_val = data[req_len-1][j];
                }
                data[req_len][srv] = min_val + 1;
            }
        }

    }

    //////////////////////////////////////
    /*for(size_t i = 0; i<servers.size(); ++i) {
        for(size_t j = 0; j<requests.size(); ++j) {
            cout<<data[j][i]<<' ';
        }
        cout<<endl;
    } // */


    // Find minimum server to start from
    int min_val = 100000000;
    for(size_t j = 0; j<servers.size(); ++j) {
        if(data[requests.size() - 1][j] < min_val)
            min_val = data[requests.size() - 1][j];
    }
    return min_val;
}

int main(int argc, char* argv[])
{
    string in_file("A-sample.in");
    if(argc > 1)
        in_file = argv[1];
    ifstream in(in_file.c_str());

    int N;
    string s;
    in>>N;
    char str[1024];
    for(size_t i = 0; i<N; ++i) {
        int n;
        vector<string> servers, requests;
        in>>n;
        in.getline(str, 1023);
        for(size_t j = 0; j<n; ++j) {
            in.getline(str, 1023);
            servers.push_back(str);
        }
        in>>n;
        in.getline(str, 1023);
        for(size_t j = 0; j<n; ++j) {
            in.getline(str, 1023);
            requests.push_back(str);
        }
        cout<<"Case #"<<i+1<<": "<<Solve(servers, requests)<<endl;
    }

    int a;
    //cin>>a;
    return 0;
}

