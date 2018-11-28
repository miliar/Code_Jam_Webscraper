#include<iostream>
//#include<vector>
#include<queue>

using namespace std;


unsigned long long int magia(queue<unsigned long long int> &q, long long int &r, long long int &k){
    unsigned long long int win = 0;
    long long int current;
    //cout<<r<<endl<<k<<endl<<q.size()<<endl;
    unsigned long long int g;

    while(r > 0){
        queue<unsigned long long int> temp;
        current = k;
        //cout<<current;
        while(current >= 0 && !q.empty() && q.front() <= current){
                g = q.front();
                q.pop();
                temp.push(g);
                win += g;
                current -= g;
        }
        while(!temp.empty()){
            q.push(temp.front());
            temp.pop();
        }
        r--;
    }
    return win;
}


int main(){
    long long int r,k,gi,win;
    unsigned int n;
    int cases;
    cin>>cases;

    for(int i=1 ; i<=cases ; i++){
        queue<unsigned long long int> q;
        win = 0;
        cin>>r>>k>>n;
        //cout<<r<<endl<<k<<endl<<n<<endl;
        for(unsigned int j=0;j<n;j++){
            cin>>gi;
            q.push(gi);
        }
        if(!q.empty())
            win = magia(q,r,k);

        cout<<"Case #"<<i<<": "<<win<<endl;

    }
    return 0;

}
