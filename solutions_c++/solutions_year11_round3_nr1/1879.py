#include<iostream>
#include<assert.h>
using namespace std;
char** create_array(int r, int c)
{
    char **a = new char *[r];
    for (int i = 0; i < r; i++)
        a[i] = new char[c];
    return a;
}

void delete_array(char ** a, int r, int c)
{
    for (int i = 0; i < r; i++)
        delete a[i];
    delete a;
}

void input_array(char ** a, int r, int c)
{
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++){
            assert(i < r && j < c);
            cin >> a[i][j];
        }
    }
}

void print_array(char ** a, int r, int c)
{
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++){
            assert(i < r && j < c);
            cout << a[i][j];
        }
        cout << endl;
    }
}

bool blue4(char ** a, int r, int c, int i, int j)
{
    if (i+1 >= r || j+1 >= c)
        return false;
    if (a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#'){
        assert(i+1 < r && j+1 < c);
        a[i][j] = a[i+1][j+1] = '/';
        a[i+1][j] = a[i][j+1] = '\\';
        return true;
    }else {
        return false;
    }
}

bool doit(char ** a, int r, int c)
{
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++){
            assert(i < r && j < c);
            if (a[i][j] == '#'){
                if (!blue4(a, r, c, i, j))
                    return false;
            }
        }
    }
    return true;
}

int main()
{
    int t, round;
    cin >> t;
    char ** pic;
    for (round = 0; round < t; round++) {
        cout << "Case #" << round+1 << ": \n";
        int r, c;
        cin >> r >> c;
        pic = create_array(r, c);
        input_array(pic, r, c);
        if (doit(pic, r, c))
           print_array(pic, r, c);
        else
            cout << "Impossible\n";
        delete_array(pic, r, c);
    }
    return 0;
}
