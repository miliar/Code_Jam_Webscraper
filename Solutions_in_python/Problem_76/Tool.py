'''
Created on May 6, 2011

@author: conan
'''
import sys, os

sample = open('sample.txt')


def getdesktop():
    '''
    Return the desktop directory
    '''
    path = os.getenv('userprofile') + '\\desktop\\'
    assert os.path.exists(path)
    return path

def ls(path):
    '''
    list files under the directory
    '''
    return os.listdir(path)
     



def transfer():
    '''
    Transfer all the input files to the corresponding directory
    '''
    for f in ls(getdesktop()):
        if ('small' in f or 'large'in f)and f.endswith('.in'):
            #Transfer from desktop to cwd
            src = getdesktop() + f
            dst = os.getcwd() + '\\' + f
            print 'Transferring from {} to {}'.format(src, dst)
            os.rename(src, dst)
    print 'Transfer is over'



if __name__ == '__main__':
    transfer()
