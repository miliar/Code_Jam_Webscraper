// mutex.h -- mutex.cpp so borland compiles as C++
#ifndef _MUTEX_H
#define _MUTEX_H
#pragma link "MutexAsm.obj"
#define waitFor(a) while(!a.acquire());

extern "C" {
   // Called when locking and testing the lock
   int EAXxchg1(int &);
   // Called when freeing the lock
   int EAXxchg0(int &);
};

class mutex{
 public:
   mutex(){
      state=0;
      //cout<<"state-init: "<<state<<endl;
   }
   ~mutex(){;}

   bool acquire(){
      int ret;
      //cout<<"state-preLock: "<<state<<endl;
      ret=EAXxchg1(state);
      //cout<<"state-postLock: "<<state<<" "<<ret<<endl;
      return ret==0;
   }
   void release(){
      //cout<<"state-preRelease: "<<state<<endl;
      state=0;
      //cout<<"state-postRelease: "<<state<<endl;
   }
 private:
   int state;
};

#endif