#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>

const double EPS = 1.0e-6f;
const double EPEPS = 1.0e-9f;

struct Seg{ double fx; double fy; double tx; double ty; int isTate; };

Seg seg[40*40*4];
int segNum = 0;

int hit[200][200];

int& getHit(int gx,int gy){
    return hit[gx + 100][gy + 100];
}

void setHit(int gx,int gy){
    getHit(gx,gy) = 1;
}

bool hasHit(int gx,int gy){
    return getHit(gx,gy) > 0;
}

int sign(double f,double eps=EPS){
    if( f >= eps ) return 1;
    if( f <= -eps ) return -1;
    return 0;
}

int round(double f){ return (int)(sign(f) * (abs(f) + 0.5f)); }
double fround(double f){ return round( f * 1.0e+6 ) * EPS; }

bool isSame(double a, double b, double eps = EPS){
    return sign(a-b,eps) == 0;
}

bool isZero(double a){ return isSame(a,0); }

bool isSame(double ax, double ay, double bx, double by, double eps = EPS){
    return isSame(ax,bx,eps) && isSame(ay,by,eps);
}

double getDD(double ax, double ay, double bx, double by){
    const double dx = ax - bx;
    const double dy = ay - by;
    return dx*dx + dy*dy;
}

double getDD(double x,double y){ return getDD(x,y,0,0); }

double getSqrtDD(double ax, double ay, double bx, double by){
    return sqrt(getDD(ax,ay,bx,by));
}

double getDot(double ax, double ay, double bx, double by){
    return ax*bx + ay*by;
}

double getCross(double ax,double ay,double bx,double by){
    return ax * by - ay * bx;
}

// �x�N�g�������s�����������������Ă��邩
bool isSameDir(double ax, double ay, double bx, double by){
    // ���ς����ŁA���A���ς̂Q�悪�����̐ς̓��Ɠ������Ȃ�S�����������������Ă���
    ax = fround(ax);
    ay = fround(ay);
    bx = fround(bx);
    by = fround(by);
    const double dot = getDot(ax,ay,bx,by);
    return sign(dot) > 0 && isSame( dot*dot, getDD(ax,ay) * getDD(bx,by), EPEPS );
}

// �x�N�g���������������w���Ă��邩�B���s�łȂ��Ă������B
bool isLikeDir(double ax, double ay, double bx, double by){
    return sign( getDot(ax,ay,bx,by) ) >= 0;
}

// ���C�ƃZ�O�����g�̏Փ˔���
bool isColSeg(double tx, double ty, double dx, double dy, Seg& s, double& rayR, double& segR, double& cx, double& cy){
    // ���C�̎n�_����Z�O�����g�n�_�ւ̃x�N�g��
    double vx,vy;
    vx = s.fx - tx;
    vy = s.fy - ty;

    double sdx = s.tx - s.fx;
    double sdy = s.ty - s.fy;

    // ���C�ƃZ�O�����g�̊O��
    double crossRaySeg = getCross(dx,dy,sdx,sdy);
    // ���C�ƃZ�O�����g�����s�Ȃ炻�������Փ˂��Ȃ�
    if( isZero(crossRaySeg) ){ return false; }

    double crossVRay = getCross(vx,vy,dx,dy);
    double crossVSeg = getCross(vx,vy,sdx,sdy);
    double t1 = crossVSeg / crossRaySeg;
    double t2 = crossVRay / crossRaySeg;
    rayR = t1;
    segR = t2;
    // �����_�������O�ɂ���ꍇ�͌����Ȃ��ƕԓ�
    if( t1 + EPS < 0 || t1 - EPS > 1 || t2 + EPS < 0 || t2 - EPS > 1 ){
        return false;
    }
    // �{���ɐ������Ō�������ꍇ�̂݌�_���v�Z
    cx = tx + dx * t1;
    cy = ty + dy * t1;
    // �܂����ˁB�܂������Ȃ��܂����ˁB
    return true;
}

// �Z�O�����g�[�_�Ɠ_�̏Փ�
bool isSegOn( Seg& s, double x, double y ){
    return isSame(s.fx,s.fy,x,y) || isSame(s.tx,s.ty,x,y);
}

void dumpHit(int D,int px, int py){
#if 0
    for(int iy = -D;iy <= D;++iy){
        if( iy == 0 ){ for(int ix = -D;ix <= D + 2;++ix){ printf("�@"); } printf("\n"); }
        for(int ix = -D;ix <= D;++ix){
            if( hasHit(px+ix,py+iy) ){
                printf("%s��%s",ix==0?"�@":"",ix==0?"�@":"");
            }else{
                printf("%s��%s",ix==0?"�@":"",ix==0?"�@":"");
            }
        }printf("\n");
        if( iy == 0 ){ for(int ix = -D;ix <= D + 2;++ix){ printf("�@"); } printf("\n"); }
    }printf("\n");
#endif
}

enum CellType {
    C_E
    , C_W
    , C_P
};

int toType( char c )
{
    switch(c)
    {
    case '.': return C_E;
    case '#': return C_W;
    case 'X': return C_P;
    }
    return C_W;
}

int main(void)
{
    int T;
    scanf("%d\n",&T);
    for(int r = 0;r < T;++r){
        printf("Case #%d: ",r+1);
        int H,W,D;
        int ans = 0;
        scanf("%d %d %d\n",&H,&W,&D);
        // �t�B�[���h�������W
        // ���Ƃ� X �����_�Ƃ��邽�߂ɑS�̂��V�t�g����K�v������v���ӁB
        int map[50][50];
        int px,py;
        for(int y = 0;y < H;++y){
            for(int x = 0;x < W;++x){
                char c;
                do{ scanf("%c",&c); }while( c == '\n' );
                map[x][y] = toType(c);
                if(map[x][y] == C_P){
                    px = x;
                    py = y;
                }
            }
        }

        // �Z�O�����g�̃��X�g�����
        segNum = 0;
        for(int y = 1;y < H;++y){
            for(int x = 1;x < W;++x){
                if( map[x][y] != C_W ){
                    // ��Ԃ̏㉺���E�ɕǂ�����΁A�������Z�O�����g�Ƃ��ēo�^
                    int v[] = {0,-1, 1,0, 0,1, -1,0};
                    bool tate[] = {false, true, false, true};
                    for(int i = 0;i < 4;++i){
                        int vx = v[i*2+0];
                        int vy = v[i*2+1];
                        if( map[x+vx][y+vy] == C_W ){
                            // �Z�O�����g���`������
                            int nvx = -vy;
                            int nvy = vx;
                            seg[segNum].fx = (double)x + 0.5f * vx - 0.5f * nvx;
                            seg[segNum].fy = (double)y + 0.5f * vy - 0.5f * nvy;
                            seg[segNum].tx = seg[segNum].fx + nvx;
                            seg[segNum].ty = seg[segNum].fy + nvy;
                            seg[segNum].isTate = tate[i];
                            //printf("(%.2f,%.2f)-(%.2f,%.2f)\n",seg[segNum].fx,seg[segNum].fy,seg[segNum].tx,seg[segNum].ty);
                            ++segNum;
                        }
                    }
                }
            }
        }

        // �Z�O�����g�ւ̃q�b�g�Ǝ����ւ̃q�b�g�̋������r���āA
        // �����ւ̃q�b�g�̕����߂���΁A�q�b�g�m��B
        
        // ���������_�Ƃ��� [-D,D] �͈̔͂������P�ŗ��U�I�ɂ���݂Ԃ��ɒ��ׂ�B
        // ���Ԃ�Ԃɍ����B
        // �����Ƀq�b�g�����ʒu�B
        for(int i = 0;i < 200;++i){
            memset(&hit[i],0,sizeof(int)*200);
        }
        for(int ilnx = -D;ilnx <= D;++ilnx){
            for(int ilny = -D;ilny <= D;++ilny){
                //if( ilnx == 5 && ilny == -1 ){
                //    printf("debug\n");
                //}
                double gnx = (double)(ilnx + px);
                double gny = (double)(ilny + py);
                // X ���g�̏ꏊ�͌��Ȃ��Ă���
                if( ilnx == 0 && ilny == 0 ) continue;
                // ���łɃq�b�g���Ă�Ȃ�������Ȃ��Ă���
                if( hasHit(gnx,gny) ) continue;
                // X ���� (gnx,gny) �Ƀ��C���΂�
                double dx = (double)(ilnx);
                double dy = (double)(ilny);
                double dd = getDD(dx,dy);
                // ��������_�͑_��Ȃ�
                if( dd > D*D ) continue;
                // �ړ��x�N�g�����v�Z
                double d = sqrt(dd);
                //dx = dx / d;
                //dy = dy / d;
                // X ����ړ��x�N�g�������ɂۂۂړ�����
                double tx = px + dx / d * 0.25f;
                double ty = py + dy / d * 0.25f;
                double remD = d - 0.25f;
                while(true){

                    // ���̃��C R(=(tx,ty)+r(dx,dy)) �� X �ƏՓ˂��邩
                    double tgx = px - tx;
                    double tgy = py - ty;
                    double hitDD = 200 * 200;
                    if( isSameDir(dx,dy,px-tx,py-ty) ){
                        // �q�b�g�������B�����́H
                        hitDD = getDD(px,py,tx,ty);
                    }

                    // ���̃��C����A�ŒZ�ŏՓ˂���Z�O�����g��������
                    double segDD = 200 * 200;
                    int nnSegID = -1;
                    double segR = 0;
                    double cx,cy;
                    double tempCx, tempCy;
                    for(int z = 0;z < segNum;++z){
                        double dr;
                        double tempSR;
                        Seg& s = seg[z];
                        if( isColSeg(tx,ty,dx,dy,s,dr,tempSR,tempCx,tempCy) ){
                            // �������������B
                            // ���߂��H
                            // �ł��닗���ł̌����͖����B
                            double tDD = getDD(tx,ty,tempCx,tempCy);
                            if( tDD < segDD && !isSame( tDD, EPEPS ) ){
                                segDD = tDD;
                                nnSegID = z;
                                segR = tempSR;
                                cx = tempCx;
                                cy = tempCy;
                            }
                        }
                    }

                    // �ŒZ�Փ˃Z�O�����g�����߂���X�ƏՓ˂��Ă���
                    // �Փ˂��m�肳����
                    if( hitDD < segDD ){
                        // ���������H
                        double segD = sqrt(hitDD);
                        if( segD > remD + EPS ){
                            // ���Ɉ��ݍ��܂ꂽ
                            break;
                        }else{
                            // ���߂łƂ�
                            // �ړ��������瓞�B�n�_���v�Z����B
                            // �v������葁��X�ɓ��B����P�[�X���J�o�[���邽�߁B
                            remD -= segD;
                            double moveD = d - remD;
                            int ax = round(px + (double)ilnx * moveD / d);
                            int ay = round(py + (double)ilny * moveD / d);
                            if( hasHit( ax, ay ) == false ){
                                setHit( ax, ay );
                                //printf("setHit:L(%d,%d) -> (%d,%d) -> (%d,%d)\n",ilnx,ilny,(int)(ilnx*moveD/d),(int)(ilny*moveD/d),ax,ay);
                                dumpHit(D,px,py);
                                ++ans;
                            }
                        }
                        break;
                    }

                    // �Z�O�����g�ɓ��Ă�
                    // �Z�O�����g�ւ̋������c��ړ������𒴂��Ă���
                    // ���ɂ��q�b�g�������̒��ɏ����Ă��܂��B
                    double segD = sqrt(segDD);
                    if( segD >= remD ){
                        // ���̒��ɏ�����
                        break;
                    }

                    // �܂������Ȃ��B
                    // �c�苗�������炷�B
                    remD -= segD;

                    // ���悢��Z�O�����g�ɏՓˁB
                    // �J�h�����肩�ۂ����m�F�B
                    if( isSame(segR,0) || isSame(segR,1) ){
                        // �Z�O�����g�̃J�h�ɓ������Ă�B
                        // �������ł��邩�ۂ��𔻒�B
                        // (cx,cy) �ɂ������Ă���Z�O�����g�����{���ł܂���������킯��B
                        // 4 -> ���܂ꂽ�Ƃ�����ؗ�ɒʂ蔲����p�^�[��
                        // 2 -> ���邩�A���˂��邩�A�ʂ蔲���邩�̕������
                        //      a. �c�c�܂��͉����Ȃ�P���̋���ȃ~���[�Ƃ݂��ĂĔ���
                        //      b. �Q�{�Ƃ������̑��ɃZ�O�����g������Ȃ�XY����
                        //      c. �P�{���������̑��ɃZ�O�����g������Ȃ�ʂ蔲��
                        //      d. ����ȊO�Ȃ����

                        // (cx,cy) �ɂ������Ă���Z�O�����g���
                        int id[8];
                        int idNum = 0;
                        for(int z = 0;z < segNum;++z){
                            if( isSegOn( seg[z], cx, cy ) ){
                                id[ idNum++ ] = z;
                            }
                        }

                        if( idNum == 4 ){
                            // �ؗ�ɃX���[
                        }else{
                            if( idNum != 2 ){
                                //printf("invalid case!!\n");
                            }else{
                                // ����ȂP���~���[�Ɣ���ł��邩�m�F
                                Seg& s1 = seg[id[0]];
                                Seg& s2 = seg[id[1]];
                                if( s1.isTate && s2.isTate ){
                                    // �c�c�̋���ȃ~���[
                                    dx = -dx;
                                }else if( !(s1.isTate) && !(s2.isTate) ){
                                    // �����̋���ȃ~���[
                                    dy = -dy;
                                }else{
                                    // XY���ˁA�X���[�A���ł̔���B
                                    // �����������ɂ��邩�A���������ɂ��邩�Ŕ���\�B
                                    // ��������\���x�N�g��
                                    double ctx = -dx;
                                    double cty = -dy;
                                    double csx,csy;
                                    if( !isSame(s1.fx,s1.fy,cx,cy) ){
                                        csx = s1.fx - cx;
                                        csy = s1.fy - cy;
                                    }else{
                                        csx = s1.tx - cx;
                                        csy = s1.ty - cy;
                                    }
                                    int likeDirNum = 0;
                                    if( isLikeDir(ctx,cty,csx,csy) ){ ++likeDirNum; }
                                    if( !isSame(s2.fx,s2.fy,cx,cy) ){
                                        csx = s2.fx - cx;
                                        csy = s2.fy - cy;
                                    }else{
                                        csx = s2.tx - cx;
                                        csy = s2.ty - cy;
                                    }
                                    if( isLikeDir(ctx,cty,csx,csy) ){ ++likeDirNum; }
                                    if( likeDirNum == 2 ){
                                        // ���S����
                                        dx = -dx;
                                        dy = -dy;
                                    }else if( likeDirNum == 1 ){
                                        // ���̂܂܃X���[
                                    }else{
                                        // ��ꂿ�����
                                        break;
                                    }
                                }
                            }
                        }
                    }else{
                        // �Z�O�����g�̃J�h�łȂ��Ƃ���ɓ��������B
                        // �c�Z�O�����g�����Z�O�����g�����m���߂�
                        // ���˂����邾���B
                        if( seg[nnSegID].isTate ){
                            dx = -dx;
                        }else{
                            dy = -dy;
                        }
                    }
                    // �ړ�
                    tx = cx + dx / d * .0f;
                    ty = cy + dy / d * .0f;
                    remD -= .0f;
                }
            }
        }
        printf("%d\n",ans);
        dumpHit(D,px,py);
    }
    return 0;
}