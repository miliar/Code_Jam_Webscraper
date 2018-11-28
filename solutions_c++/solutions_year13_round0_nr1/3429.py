// normal_distribution
#include <iostream>
#include <random>
#include <fstream>
using namespace std;



class Matrix {
public:
  Matrix(unsigned rows, unsigned cols);
  char& operator() (unsigned row, unsigned col);
  char  operator() (unsigned row, unsigned col) const;
   ~Matrix();                              // Destructor
  Matrix(Matrix const& m);               // Copy constructor
  Matrix& operator= (Matrix const& m);   // Assignment operator

private:
  unsigned rows_, cols_;
  char* data_;
};

inline
Matrix::Matrix(unsigned rows, unsigned cols)
  : rows_ (rows)
  , cols_ (cols)
  //data_ <--initialized below (after the 'if/throw' statement)
{
  //if (rows == 0 || cols == 0)
    //throw BadIndex("Matrix constructor has 0 size");
  data_ = new char[rows * cols];
}

inline
Matrix::~Matrix()
{
  delete[] data_;
}

inline
char& Matrix::operator() (unsigned row, unsigned col)
{
  //if (row >= rows_ || col >= cols_)
    //throw BadIndex("Matrix subscript out of bounds");
  return data_[cols_*row + col];
}

inline
char Matrix::operator() (unsigned row, unsigned col) const
{
  //if (row >= rows_ || col >= cols_)
    //throw BadIndex("const Matrix subscript out of bounds");
  return data_[cols_*row + col];
}

bool checkhori(int i0, int j0, Matrix& mat, char S){
    if(mat(i0,j0)==S||mat(i0,j0)=='T'){
        if(j0==3)
            return true;
        else
            return checkhori(i0,j0+1,mat,S);
    }
    else
        return false;
}

bool checkverti(int i0, int j0, Matrix& mat, char S){
    if(mat(i0,j0)==S||mat(i0,j0)=='T'){
        if(i0==3)
            return true;
        else
            return checkverti(i0+1,j0,mat,S);
    }
    else
        return false;
}


bool checkdiag1(int i0, int j0, Matrix& mat, char S){
    if(mat(i0,j0)==S||mat(i0,j0)=='T'){
        if(i0==3)
            return true;
        else
            return checkdiag1(i0+1,j0+1,mat,S);
    }
    else
        return false;
}


bool checkdiag2(int i0, int j0, Matrix& mat, char S){
    if(mat(i0,j0)==S||mat(i0,j0)=='T'){
        if(j0==3)
            return true;
        else
            return checkdiag2(i0-1,j0+1,mat,S);
    }
    else
        return false;
}


int main(){
    ifstream in("A-large.in");
    ofstream cout("output.txt");
    //istream& in=cin;
    int N;
    in>>N;
    for(int n=0;n<N;n++){
        Matrix mat(4,4);
        bool Xwin=false;
        bool Owin=false;
        bool HasDot=false;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                in>>mat(i,j);
                if(mat(i,j)=='.')
                    HasDot=true;
            }
        }

        cout<<"Case #"<<n+1<<": ";

    //begin check
    //check horizon first
        Xwin=checkhori(0,0,mat,'X')||checkhori(1,0,mat,'X')||checkhori(2,0,mat,'X')||checkhori(3,0,mat,'X')
           ||checkverti(0,0,mat,'X')||checkverti(0,1,mat,'X')||checkverti(0,2,mat,'X')||checkverti(0,3,mat,'X')
           ||checkdiag1(0,0,mat,'X')||checkdiag2(3,0,mat,'X');
        Owin=checkhori(0,0,mat,'O')||checkhori(1,0,mat,'O')||checkhori(2,0,mat,'O')||checkhori(3,0,mat,'O')
           ||checkverti(0,0,mat,'O')||checkverti(0,1,mat,'O')||checkverti(0,2,mat,'O')||checkverti(0,3,mat,'O')
           ||checkdiag1(0,0,mat,'O')||checkdiag2(3,0,mat,'O');
        if(  Xwin   )
            cout<<"X won"<<endl;
        else if(Owin)
            cout<<"O won"<<endl;
        else if(HasDot)
            cout<<"Game has not completed"<<endl;
        else
            cout<<"Draw"<<endl;





//        for(int i=0;i<4;i++){
//            for(int j=0;j<4;j++)
//                cout<<mat(i,j);
//        }

    }




    return 0;
}
