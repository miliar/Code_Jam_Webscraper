/*
    Author : Akai
    Problem : B
*/

#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>

using namespace std;

void search(int now , int dep , int Len , int tot){
     if (dep == n){
             ans = max(ans , min(len , tot)) ;
     }
     for (int i = 1 ; i <= 10  ; i++) if (!vis[i]){
         
     
     

int main(){
    scanf("%d" , &T);
    while (T--){
          scanf("%d" , &n);
          for (int i = 1; i <= n ; i++) scanf("%d" , &a[i]);
          search(-1 , 0  , 0 , 100); 
