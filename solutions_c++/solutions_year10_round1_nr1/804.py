#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int N, K;
        cin >> N >> K;
        char* mm = new char[N*N];
        memset(mm, 0, N*N*sizeof(*mm));
        char** m = new char*[N];
        m[0] = mm;
        for (int i=0; i<N; ++i)
            m[i+1] = m[i] + N;
        for (int r=0; r<N; ++r) {
            string s;
            cin >> s;
            for (int c=N-1, k=0; c>=0; --c) 
                if (s[c] != '.')
                    m[r][k++] = s[c];
        }

        int red=0, blue=0;

        for (int r=0; r<N; ++r) {
            int run=0;
            char state=0;
            for (int c=0; c<N; ++c) {
                if (state && state == m[r][c]) {
                    ++run;
                    if (run == K) {
                        if (state == 'R') red = 1;
                        else if (state == 'B') blue = 1;
                    }
                } else {
                    state = m[r][c];
                    run = 1;
                }
            }
        }

        for (int c=0; c<N; ++c) {
            int run=0;
            char state=0;
            for (int r=0; r<N; ++r) {
                if (state && state == m[r][c]) {
                    ++run;
                    if (run == K) {
                        if (state == 'R') red = 1;
                        else if (state == 'B') blue = 1;
                    }
                } else {
                    state = m[r][c];
                    run = 1;
                }
            }
        }

        for (int d=0; d<N; ++d) {
            int run=0;
            char state=0;
            for (int r=d, c=0; r>=0; --r, ++c) {
                if (state && state == m[r][c]) {
                    ++run;
                    if (run == K) {
                        if (state == 'R') red = 1;
                        else if (state == 'B') blue = 1;
                    }
                } else {
                    state = m[r][c];
                    run = 1;
                }
            }
        }

        for (int d=1; d<N; ++d) {
            int run=0;
            char state=0;
            for (int c=d, r=N-1; c<N; --r, ++c) {
                if (state && state == m[r][c]) {
                    ++run;
                    if (run == K) {
                        if (state == 'R') red = 1;
                        else if (state == 'B') blue = 1;
                    }
                } else {
                    state = m[r][c];
                    run = 1;
                }
            }
        }

        for (int d=0; d<N; ++d) {
            int run=0;
            char state=0;
            for (int r=N-1-d, c=0; r<N && c<N; ++r, ++c) {
                if (state && state == m[r][c]) {
                    ++run;
                    if (run == K) {
                        if (state == 'R') red = 1;
                        else if (state == 'B') blue = 1;
                    }
                } else {
                    state = m[r][c];
                    run = 1;
                }
            }
        }

        for (int d=1; d<N; ++d) {
            int run=0;
            char state=0;
            for (int c=d, r=0; c<N && r<N; ++r, ++c) {
                if (state && state == m[r][c]) {
                    ++run;
                    if (run == K) {
                        if (state == 'R') red = 1;
                        else if (state == 'B') blue = 1;
                    }
                } else {
                    state = m[r][c];
                    run = 1;
                }
            }
        }

        cout << "Case #" << cs << ": ";
        if (red && blue) cout << "Both";
        else if (red) cout << "Red";
        else if (blue) cout << "Blue";
        else cout << "Neither";
        cout << "\n";
    }
}
