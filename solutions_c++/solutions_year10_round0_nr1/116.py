/*
 * =====================================================================================
 *
 *       Filename:  1.cpp
 *
 *    Description:  1
 *
 *        Version:  0.0
 *        Created:  05/08/2010 09:29:45 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Jianfei Wang (thinXer), me@thinxer.com
 *        Company:  Tsinghua University
 *
 * =====================================================================================
 */

#include	<iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int a,b;
        cin >> a >> b;
        cout << "Case #" << (i+1) << ": " << (((b%(1<<a)) == (1<<a) - 1)?"ON":"OFF") << endl;
    }
    return 0;
}
