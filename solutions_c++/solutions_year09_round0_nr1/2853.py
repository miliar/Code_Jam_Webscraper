#include <iostream>
#include <string>

using namespace std;

class a
{protected:
      int f(){
          return 1;
          }
};

class b : public a
{
};

class c : public b
{public:
      int f1()
      {
          return f();
      }
};

int main()
{
    c c1;
    //cout<<" value is : "<<c1.f1()<<endl;
    string t = "Failed to set the Acquirer Message Type Identifier (MTI) TDE to <5" \
"> in <4>() called by interface <1> (Subsystem Identifer: <2>) while trying" \
" to <3> a message.                                                        " \
"                                          ";
    string t2 = "Failed to set the Acquirer Message Type Identifier (MTI) TDE to " \
"<5> in <4>() called by interface <1> (Subsystem Identifer: <2>) while tryi" \
"ng to <3> a message.                                                      " \
"                                            ";
    cout<<"length = "<<t2.size();
    getchar();
    return 1;
}
