#include <iostream>

using namespace std;

int C;

int M;
bool V;

int values[10001];

int intGs[10001];
int intCs[10001];

int swapped[10001];

int minChanged;


bool recurse(int root)
{
    //cout << root << " " << values[root] << endl;
    
    int lchild = ((1+root)*2)-1;
    
    if(values[root] != -1)
    {
        return values[root];
    }
    
    if(intGs[root] == 1)
    {
        /// And
        values[root] = recurse(lchild)&&recurse(lchild+1);
    }
    else
    {
        /// Or
        values[root] = recurse(lchild)||recurse(lchild+1);
    }
    
    /*
    if(swapped[root])
        values[root] = !values[root];
    */
    return values[root];
}


void choosePermutation(int a, int numChanged)
{
    if(numChanged >= minChanged)
        return;
    
    int limInt = (M-1)/2;
    
    for(int i = 0; i < limInt; ++i)
        values[i] = -1;
    
    if(recurse(0)==V)
    {
        //cout << a << " " << numChanged << endl;
        
        minChanged = numChanged;
        return;
    }
    
    
    
    for(int i = a; i < limInt; ++i)
    {
        if(intCs[i] == 1)
        {
            intGs[i] = !intGs[i];
            //swapped[i] = true;
            choosePermutation(i+1, numChanged+1);
            intGs[i] = !intGs[i];
            //swapped[i] = false;
            choosePermutation(i+1, numChanged);
        }
    }
    
    
}




int main()
{
    cin >> C;
    
    for(int i = 1; i <= C; ++i)
    {
        cin >> M >> V;
        
        int limInt = (M-1)/2;
        minChanged = 1000;
        
        for(int j = 0; j < limInt; ++j)
        {
            cin >> intGs[j] >> intCs[j];
            values[j] = -1;
            swapped[j] = false;
            
        }
        
        for(int j = limInt; j < M; ++j)
        {
            cin >> values[j];
        }
        
        choosePermutation(0, 0);
        
        if(minChanged == 1000)
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i << ": " << minChanged << endl;
        
    }
    
}

